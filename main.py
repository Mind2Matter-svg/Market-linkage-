from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import math

app = FastAPI(
    title="KrishiLink API - Mind2Matter (SIH26132)",
    description="Backend API for Price Discovery, 3-Way Lot Management, and Net Profit Recommendation Engine",
    version="1.0.0"
)

# Enable CORS so your frontend prototype can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# DATA MODELS (Pydantic Schemas)
# ==========================================

class LotType(str, Enum):
    MARKET = "Market"
    BUYER = "Buyer"
    STORAGE = "Storage"

class CropGrade(str, Enum):
    GRADE_A = "Grade A"
    GRADE_B = "Grade B"
    GRADE_C = "Grade C"

class LotCreateRequest(BaseModel):
    farmer_id: str = "FARMER_101"
    farmer_location: str = "Karnaal, Haryana"
    crop_name: str = "Wheat"
    quantity_quintals: float = Field(..., gt=0, description="Quantity in Quintals")
    grade: CropGrade = CropGrade.GRADE_A
    lot_type: LotType = LotType.MARKET
    expected_base_price: Optional[float] = 2350.0

class SellingOption(BaseModel):
    option_type: str
    destination_name: str
    distance_km: float
    gross_price_per_qtl: float
    total_gross_value: float
    transport_and_handling_cost: float
    expected_net_profit: float
    recommendation_score: float

class RecommendationResponse(BaseModel):
    crop_name: str
    quantity_quintals: float
    top_recommendation: str
    options: List[SellingOption]

# ==========================================
# MOCK DATASETS & API SIMULATION
# ==========================================

# Simulated AGMARKNET Mandi Price Database
MOCK_MANDI_DATA = [
    {"name": "Karnaal Main APMC Mandi", "distance_km": 28.0, "base_price": 2380.0, "mandi_fee_pct": 0.02},
    {"name": "Panipat Grain Market", "distance_km": 45.0, "base_price": 2420.0, "mandi_fee_pct": 0.02},
    {"name": "Ambala Wholesale Market", "distance_km": 65.0, "base_price": 2450.0, "mandi_fee_pct": 0.025},
]

# Simulated Verified Buyers
MOCK_BUYER_DATA = [
    {"name": "BigBasket Procurement", "distance_km": 12.0, "offered_price": 2450.0, "pickup_fee": 5000.0},
    {"name": "Reliable Agro Traders", "distance_km": 20.0, "offered_price": 2420.0, "pickup_fee": 3500.0},
]

# Simulated Storage Facilities
MOCK_STORAGE_DATA = [
    {"name": "AgriSecure Cold Warehouse", "distance_km": 15.0, "future_projected_price": 2600.0, "rent_per_qtl_month": 150.0},
]

# ==========================================
# API ENDPOINTS
# ==========================================

@app.get("/")
def root():
    return {
        "status": "Online",
        "project": "SIH26132 - Smart Market Linkage",
        "team": "Mind2Matter",
        "docs_url": "/docs"
    }

@app.post("/api/v1/lots/create", response_model=dict)
def create_lot(lot: LotCreateRequest):
    """
    Creates a new Market, Buyer, or Storage Lot for the farmer.
    """
    # In production, save `lot` object into MySQL / MongoDB
    lot_id = f"LOT-{math.floor(1000 + math.fmod(hash(lot.crop_name), 9000))}"
    
    return {
        "status": "Success",
        "message": f"{lot.lot_type.value} Lot created successfully.",
        "lot_id": lot_id,
        "details": lot
    }

@app.post("/api/v1/recommendations/analyze", response_model=RecommendationResponse)
def get_selling_recommendations(lot: LotCreateRequest):
    """
    Recommendation Engine: Calculates net profit across Mandis, Buyers, and Storage facilities 
    by evaluating prices against distance, transportation rates, and fees.
    """
    qty = lot.quantity_quintals
    transport_rate_per_km_qtl = 3.5  # Transport cost per KM per Quintal

    options: List[SellingOption] = []

    # 1. Calculate APMC Mandis (Market Lot)
    for mandi in MOCK_MANDI_DATA:
        gross_val = mandi["base_price"] * qty
        transport_cost = mandi["distance_km"] * transport_rate_per_km_qtl * (qty / 10)
        mandi_fee = gross_val * mandi["mandi_fee_pct"]
        total_deduction = transport_cost + mandi_fee
        net_profit = gross_val - total_deduction

        options.append(SellingOption(
            option_type="APMC Mandi",
            destination_name=mandi["name"],
            distance_km=mandi["distance_km"],
            gross_price_per_qtl=mandi["base_price"],
            total_gross_value=gross_val,
            transport_and_handling_cost=round(total_deduction, 2),
            expected_net_profit=round(net_profit, 2),
            recommendation_score=net_profit
        ))

    # 2. Calculate Direct Verified Buyers (Buyer Lot)
    for buyer in MOCK_BUYER_DATA:
        gross_val = buyer["offered_price"] * qty
        total_deduction = buyer["pickup_fee"]
        net_profit = gross_val - total_deduction

        options.append(SellingOption(
            option_type="Verified Buyer",
            destination_name=buyer["name"],
            distance_km=buyer["distance_km"],
            gross_price_per_qtl=buyer["offered_price"],
            total_gross_value=gross_val,
            transport_and_handling_cost=round(total_deduction, 2),
            expected_net_profit=round(net_profit, 2),
            recommendation_score=net_profit
        ))

    # 3. Calculate Storage Options (Storage Lot - Projected 30-Day Hold)
    for storage in MOCK_STORAGE_DATA:
        gross_val = storage["future_projected_price"] * qty
        storage_rent = storage["rent_per_qtl_month"] * qty
        transport_cost = storage["distance_km"] * transport_rate_per_km_qtl * (qty / 10)
        total_deduction = storage_rent + transport_cost
        net_profit = gross_val - total_deduction

        options.append(SellingOption(
            option_type="Storage Facility (30 Days Hold)",
            destination_name=storage["name"],
            distance_km=storage["distance_km"],
            gross_price_per_qtl=storage["future_projected_price"],
            total_gross_value=gross_val,
            transport_and_handling_cost=round(total_deduction, 2),
            expected_net_profit=round(net_profit, 2),
            recommendation_score=net_profit
        ))

    # Sort options by highest net profit first
    options.sort(key=lambda x: x.expected_net_profit, reverse=True)

    return RecommendationResponse(
        crop_name=lot.crop_name,
        quantity_quintals=qty,
        top_recommendation=options[0].destination_name,
        options=options
    )
