from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Optional
import sqlite3
import hashlib

app = FastAPI(
    title="KisanSetu Backend",
    description="Backend API for Farmer Market Linkage and Price Discovery",
    version="1.0.0"
)

DATABASE = "kisansetu.db"


# ---------------- DATABASE ----------------

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS lots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            crop TEXT,
            quantity REAL,
            price REAL,
            capacity REAL,
            description TEXT,
            created_by INTEGER
        )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------------- MODELS ----------------

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str = "farmer"


class LoginRequest(BaseModel):
    email: str
    password: str


class LotCreate(BaseModel):
    type: Literal["market", "buyer", "storage"]
    name: str
    location: str
    crop: Optional[str] = None
    quantity: Optional[float] = Field(default=None, ge=0)
    price: Optional[float] = Field(default=None, ge=0)
    capacity: Optional[float] = Field(default=None, ge=0)
    description: Optional[str] = None
    created_by: Optional[int] = None


# ---------------- HOME ----------------

@app.get("/")
def home():
    return {
        "message": "KisanSetu Backend is running",
        "status": "success"
    }


# ---------------- REGISTER ----------------

@app.post("/api/register")
def register(user: RegisterRequest):

    conn = get_db()

    existing_user = conn.execute(
        "SELECT id FROM users WHERE email = ?",
        (user.email,)
    ).fetchone()

    if existing_user:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    password_hash = hashlib.sha256(
        user.password.encode()
    ).hexdigest()

    cursor = conn.execute(
        """
        INSERT INTO users (name, email, password, role)
        VALUES (?, ?, ?, ?)
        """,
        (
            user.name,
            user.email,
            password_hash,
            user.role
        )
    )

    conn.commit()

    user_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Registration successful",
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }


# ---------------- LOGIN ----------------

@app.post("/api/login")
def login(user: LoginRequest):

    password_hash = hashlib.sha256(
        user.password.encode()
    ).hexdigest()

    conn = get_db()

    result = conn.execute(
        """
        SELECT id, name, email, role
        FROM users
        WHERE email = ? AND password = ?
        """,
        (
            user.email,
            password_hash
        )
    ).fetchone()

    conn.close()

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "user": {
            "id": result["id"],
            "name": result["name"],
            "email": result["email"],
            "role": result["role"]
        }
    }


# ---------------- CREATE LOT ----------------

@app.post("/api/lots")
def create_lot(lot: LotCreate):

    conn = get_db()

    cursor = conn.execute(
        """
        INSERT INTO lots
        (type, name, location, crop, quantity, price,
         capacity, description, created_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            lot.type,
            lot.name,
            lot.location,
            lot.crop,
            lot.quantity,
            lot.price,
            lot.capacity,
            lot.description,
            lot.created_by
        )
    )

    conn.commit()

    lot_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Lot created successfully",
        "lot_id": lot_id,
        "lot": lot.model_dump()
    }


# ---------------- VIEW LOTS ----------------

@app.get("/api/lots")
def view_lots(
    type: Optional[Literal["market", "buyer", "storage"]] = None
):

    conn = get_db()

    if type:
        rows = conn.execute(
            "SELECT * FROM lots WHERE type = ?",
            (type,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM lots"
        ).fetchall()

    conn.close()

    return {
        "count": len(rows),
        "lots": [dict(row) for row in rows]
  }
