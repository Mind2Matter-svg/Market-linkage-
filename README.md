# frontend 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIH26132 - Mind2Matter | Farmer Price Discovery & Market Linkage Prototype</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .active-tab { border-bottom: 3px solid #16a34a; color: #16a34a; font-weight: bold; }
        .lot-card:hover { transform: translateY(-2px); transition: all 0.2s ease; }
    </style>
</head>
<body class="bg-gray-100 font-sans min-h-screen flex flex-col">

    <!-- Top Header -->
    <header class="bg-green-700 text-white shadow-lg sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <i class="fa-solid fa-wheat-awn text-2xl text-yellow-300"></i>
                <div>
                    <h1 class="text-xl font-bold tracking-wide">KrishiLink | Kisan Portal</h1>
                    <p class="text-xs text-green-200">SIH26132 • Team Mind2Matter</p>
                </div>
            </div>
            
            <!-- Voice Assistant & Language Toggle -->
            <div class="flex items-center space-x-3">
                <button onclick="speakPageInfo()" class="bg-yellow-500 hover:bg-yellow-600 text-gray-900 font-semibold px-3 py-1.5 rounded-full text-xs flex items-center space-x-2 shadow transition">
                    <i class="fa-solid fa-volume-high text-base"></i>
                    <span id="voice-btn-text">Listen / सुनो</span>
                </button>

                <select id="lang-select" onchange="switchLanguage()" class="bg-green-800 text-white text-xs px-2 py-1.5 rounded border border-green-600 focus:outline-none">
                    <option value="en">English</option>
                    <option value="hi">हिन्दी (Hindi)</option>
                </select>
            </div>
        </div>
    </header>

    <!-- Main Navigation Bar -->
    <nav class="bg-white border-b border-gray-200 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 flex justify-around md:justify-start space-x-1 md:space-x-8 text-sm">
            <button onclick="switchTab('create-lot')" id="tab-create-lot" class="py-3 px-2 active-tab flex items-center space-x-2">
                <i class="fa-solid fa-plus-circle text-lg"></i>
                <span data-en="Create Lot" data-hi="नया लॉट बनाएं">Create Lot</span>
            </button>
            <button onclick="switchTab('recommendations')" id="tab-recommendations" class="py-3 px-2 text-gray-600 flex items-center space-x-2">
                <i class="fa-solid fa-chart-line text-lg"></i>
                <span data-en="Recommendations" data-hi="बिक्री की सलाह">Recommendations</span>
            </button>
            <button onclick="switchTab('buyer-offers')" id="tab-buyer-offers" class="py-3 px-2 text-gray-600 flex items-center space-x-2">
                <i class="fa-solid fa-handshake text-lg"></i>
                <span data-en="Buyer Offers" data-hi="खरीदार के प्रस्ताव">Buyer Offers</span>
            </button>
            <button onclick="switchTab('transactions')" id="tab-transactions" class="py-3 px-2 text-gray-600 flex items-center space-x-2">
                <i class="fa-solid fa-file-invoice-dollar text-lg"></i>
                <span data-en="Transactions" data-hi="लेनदेन एवं स्थिति">Transactions</span>
            </button>
        </div>
    </nav>

    <!-- Main Content Container -->
    <main class="max-w-6xl mx-auto px-4 py-6 flex-grow w-full">

        <!-- ================= TAB 1: CREATE THREE-WAY LOT ================= -->
        <section id="sec-create-lot" class="space-y-6">
            <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
                <div class="flex items-center justify-between mb-4">
                    <h2 class="text-lg font-bold text-gray-800 flex items-center gap-2">
                        <i class="fa-solid fa-boxes-stacked text-green-600"></i>
                        <span data-en="Step 1: Select Your Lot Purpose (3-Way System)" data-hi="चरण 1: अपने लॉट का प्रकार चुनें">Step 1: Select Your Lot Purpose (3-Way System)</span>
                    </h2>
                    <span class="text-xs bg-green-100 text-green-800 font-medium px-2.5 py-0.5 rounded-full">Innovation Feature</span>
                </div>

                <!-- 3-Way Lot Cards -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    <!-- Market Lot -->
                    <div id="lot-type-market" onclick="selectLotType('Market')" class="cursor-pointer p-4 rounded-lg border-2 border-green-500 bg-green-50/50 hover:bg-green-50 transition relative">
                        <div class="flex items-center space-x-3 mb-2">
                            <i class="fa-solid fa-building-wheat text-2xl text-green-600"></i>
                            <h3 class="font-bold text-gray-800" data-en="1. Market Lot" data-hi="1. मंडी लॉट">1. Market Lot</h3>
                        </div>
                        <p class="text-xs text-gray-600" data-en="List directly for APMC Mandis / AGMARKNET prices." data-hi="निकटतम APMC मंडी और AGMARKNET भाव देखने हेतु।">List directly for APMC Mandis / AGMARKNET prices.</p>
                        <input type="radio" name="lotType" value="Market" class="absolute top-4 right-4 accent-green-600" checked>
                    </div>

                    <!-- Buyer Lot -->
                    <div id="lot-type-buyer" onclick="selectLotType('Buyer')" class="cursor-pointer p-4 rounded-lg border-2 border-gray-200 hover:border-green-500 hover:bg-green-50 transition relative">
                        <div class="flex items-center space-x-3 mb-2">
                            <i class="fa-solid fa-truck-ramp-box text-2xl text-blue-600"></i>
                            <h3 class="font-bold text-gray-800" data-en="2. Buyer Lot" data-hi="2. खरीदार लॉट">2. Buyer Lot</h3>
                        </div>
                        <p class="text-xs text-gray-600" data-en="Receive direct bids/offers from verified buyers." data-hi="सत्यापित खरीदारों से सीधे प्रस्ताव प्राप्त करें।">Receive direct bids/offers from verified buyers.</p>
                        <input type="radio" name="lotType" value="Buyer" class="absolute top-4 right-4 accent-green-600">
                    </div>

                    <!-- Storage Lot -->
                    <div id="lot-type-storage" onclick="selectLotType('Storage')" class="cursor-pointer p-4 rounded-lg border-2 border-gray-200 hover:border-green-500 hover:bg-green-50 transition relative">
                        <div class="flex items-center space-x-3 mb-2">
                            <i class="fa-solid fa-warehouse text-2xl text-amber-600"></i>
                            <h3 class="font-bold text-gray-800" data-en="3. Storage Lot" data-hi="3. भंडारण लॉट">3. Storage Lot</h3>
                        </div>
                        <p class="text-xs text-gray-600" data-en="Store produce in nearby cold storage for future selling." data-hi="भविष्य में बेहतर दाम हेतु नजदीकी गोदाम/कोल्ड स्टोरेज में रखें।">Store produce in nearby cold storage for future selling.</p>
                        <input type="radio" name="lotType" value="Storage" class="absolute top-4 right-4 accent-green-600">
                    </div>
                </div>

                <!-- Lot Details Form -->
                <form id="lot-form" onsubmit="handleLotSubmit(event)" class="space-y-4">
                    <h2 class="text-md font-bold text-gray-800 mb-2" data-en="Step 2: Enter Produce Details" data-hi="चरण 2: फसल का विवरण भरें">Step 2: Enter Produce Details</h2>
                    
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div>
                            <label class="block text-xs font-semibold text-gray-700 mb-1" data-en="Select Crop" data-hi="फसल चुनें">Select Crop</label>
                            <select id="crop-select" class="w-full border border-gray-300 p-2.5 rounded-lg text-sm focus:ring-2 focus:ring-green-500 focus:outline-none">
                                <option value="Wheat">🌾 Wheat (गेहूँ)</option>
                                <option value="Rice">🌾 Paddy / Rice (धान / चावल)</option>
                                <option value="Tomato">🍅 Tomato (टमाटर)</option>
                                <option value="Potato">🥔 Potato (आलू)</option>
                                <option value="Onion">🧅 Onion (प्याज)</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-gray-700 mb-1" data-en="Quantity (Quintals)" data-hi="मात्रा (क्विंटल में)">Quantity (Quintals)</label>
                            <input type="number" id="lot-qty" value="50" min="1" required class="w-full border border-gray-300 p-2 rounded-lg text-sm focus:ring-2 focus:ring-green-500 focus:outline-none">
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-gray-700 mb-1" data-en="Quality Grade" data-hi="गुणवत्ता ग्रेड">Quality Grade</label>
                            <select id="lot-grade" class="w-full border border-gray-300 p-2.5 rounded-lg text-sm focus:ring-2 focus:ring-green-500 focus:outline-none">
                                <option value="Grade A">Grade A (Premium / उत्तम)</option>
                                <option value="Grade B">Grade B (Standard / सामान्य)</option>
                                <option value="Grade C">Grade C (Fair / मध्यम)</option>
                            </select>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                        <div>
                            <label class="block text-xs font-semibold text-gray-700 mb-1" data-en="Farmer Location (GPS / Village)" data-hi="किसान का स्थान (गाँव / स्थान)">Farmer Location (GPS / Village)</label>
                            <div class="flex space-x-2">
                                <input type="text" id="farmer-location" value="Karnaal, Haryana" class="w-full border border-gray-300 p-2 rounded-lg text-sm">
                                <button type="button" class="bg-gray-200 hover:bg-gray-300 text-gray-700 px-3 rounded-lg text-xs flex items-center">
                                    <i class="fa-solid fa-location-dot mr-1"></i> GPS
                                </button>
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-gray-700 mb-1" data-en="Expected Base Price (₹/Quintal)" data-hi="अपेक्षित न्यूनतम मूल्य (₹/क्विंटल)">Expected Base Price (₹/Quintal)</label>
                            <input type="number" id="base-price" value="2350" class="w-full border border-gray-300 p-2 rounded-lg text-sm">
                        </div>
                    </div>

                    <button type="submit" class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 rounded-lg shadow-md transition flex items-center justify-center space-x-2">
                        <i class="fa-solid fa-wand-magic-sparkles"></i>
                        <span data-en="Create Lot & Get Selling Recommendations" data-hi="लॉट बनाएं और सर्वश्रेष्ठ विकल्प देखें">Create Lot & Get Selling Recommendations</span>
                    </button>
                </form>
            </div>
        </section>

        <!-- ================= TAB 2: RECOMMENDATION ENGINE ================= -->
        <section id="sec-recommendations" class="space-y-6 hidden">
            <div class="bg-gradient-to-r from-green-800 to-green-900 text-white p-5 rounded-xl shadow-md flex justify-between items-center">
                <div>
                    <span class="text-xs bg-yellow-400 text-gray-900 px-2 py-0.5 rounded font-bold uppercase" data-en="Smart Recommendation Engine" data-hi="स्मार्ट सलाह प्रणाली">Smart Recommendation Engine</span>
                    <h2 class="text-lg font-bold mt-1" id="rec-summary-title">Analyzing options for Wheat (50 Quintals - Grade A)</h2>
                    <p class="text-xs text-green-200" data-en="Calculated based on AGMARKNET live prices, OSRM distance, & transport cost." data-hi="AGMARKNET लाइव भाव, OSRM दूरी और परिवहन लागत के आधार पर गणना।">Calculated based on AGMARKNET live prices, OSRM distance, & transport cost.</p>
                </div>
                <button onclick="speakText('Our recommendation engine suggests selling directly to BigBasket Verified Buyer for the highest net profit of 1 lakh 17 thousand rupees after transport deduction.')" class="bg-white/20 hover:bg-white/30 text-white p-2.5 rounded-full">
                    <i class="fa-solid fa-volume-high text-xl"></i>
                </button>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6" id="recommendation-cards">
                <!-- Top Pick: Verified Buyer Option -->
                <div class="bg-white rounded-xl shadow-lg border-2 border-green-500 p-5 relative flex flex-col justify-between">
                    <div class="absolute -top-3 right-4 bg-green-600 text-white text-xs px-3 py-1 rounded-full font-bold shadow">
                        ⭐ Best Net Profit
                    </div>
                    <div>
                        <div class="flex items-center space-x-2 text-green-700 font-bold text-sm mb-1">
                            <i class="fa-solid fa-user-check"></i>
                            <span>Verified Direct Buyer</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900">BigBasket Procurement</h3>
                        <p class="text-xs text-gray-500 mb-3"><i class="fa-solid fa-route"></i> Distance: 12 km (Pick-up at farm available)</p>
                        
                        <div class="bg-gray-50 p-3 rounded-lg space-y-1 text-xs mb-4">
                            <div class="flex justify-between"><span>Offered Price:</span> <span class="font-bold text-gray-800">₹2,450 / Qtl</span></div>
                            <div class="flex justify-between"><span>Total Gross Value:</span> <span>₹1,22,500</span></div>
                            <div class="flex justify-between text-red-600"><span>Transport / Handling:</span> <span>- ₹5,000</span></div>
                            <hr class="my-1">
                            <div class="flex justify-between text-sm font-bold text-green-700"><span>Expected Net Profit:</span> <span>₹1,17,500</span></div>
                        </div>
                    </div>
                    <button onclick="acceptRecommendation('BigBasket Procurement', '₹1,17,500')" class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 rounded-lg text-sm transition">
                        Select Buyer & Confirm Deal
                    </button>
                </div>

                <!-- Option 2: Nearest APMC Mandi -->
                <div class="bg-white rounded-xl shadow border border-gray-200 p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center space-x-2 text-blue-700 font-bold text-sm mb-1">
                            <i class="fa-solid fa-building-wheat"></i>
                            <span>APMC Mandi (AGMARKNET)</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900">Karnaal Main Mandi</h3>
                        <p class="text-xs text-gray-500 mb-3"><i class="fa-solid fa-route"></i> Distance: 28 km</p>
                        
                        <div class="bg-gray-50 p-3 rounded-lg space-y-1 text-xs mb-4">
                            <div class="flex justify-between"><span>Mandi Price (Avg):</span> <span class="font-bold text-gray-800">₹2,380 / Qtl</span></div>
                            <div class="flex justify-between"><span>Total Gross Value:</span> <span>₹1,19,000</span></div>
                            <div class="flex justify-between text-red-600"><span>Transport + Mandi Fee:</span> <span>- ₹8,200</span></div>
                            <hr class="my-1">
                            <div class="flex justify-between text-sm font-bold text-blue-800"><span>Expected Net Profit:</span> <span>₹1,10,800</span></div>
                        </div>
                    </div>
                    <button onclick="acceptRecommendation('Karnaal Main Mandi', '₹1,10,800')" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded-lg text-sm transition">
                        Choose APMC Mandi
                    </button>
                </div>

                <!-- Option 3: Storage Option -->
                <div class="bg-white rounded-xl shadow border border-gray-200 p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center space-x-2 text-amber-700 font-bold text-sm mb-1">
                            <i class="fa-solid fa-warehouse"></i>
                            <span>Cold Storage / Warehouse</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900">AgriSecure Warehouse</h3>
                        <p class="text-xs text-gray-500 mb-3"><i class="fa-solid fa-clock"></i> Hold for 30 Days (Price Trend ↑ +8%)</p>
                        
                        <div class="bg-gray-50 p-3 rounded-lg space-y-1 text-xs mb-4">
                            <div class="flex justify-between"><span>Projected Price:</span> <span class="font-bold text-gray-800">₹2,600 / Qtl</span></div>
                            <div class="flex justify-between"><span>Projected Value:</span> <span>₹1,30,000</span></div>
                            <div class="flex justify-between text-red-600"><span>Rent & Handling (30 days):</span> <span>- ₹9,500</span></div>
                            <hr class="my-1">
                            <div class="flex justify-between text-sm font-bold text-amber-800"><span>Projected Net Profit:</span> <span>₹1,20,500</span></div>
                        </div>
                    </div>
                    <button onclick="acceptRecommendation('AgriSecure Warehouse', '₹1,20,500')" class="w-full bg-amber-600 hover:bg-amber-700 text-white font-semibold py-2 rounded-lg text-sm transition">
                        Reserve Storage Slot
                    </button>
                </div>
            </div>
        </section>

        <!-- ================= TAB 3: BUYER OFFERS & NEGOTIATION ================= -->
        <section id="sec-buyer-offers" class="space-y-6 hidden">
            <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
                <h2 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-comments-dollar text-green-600"></i>
                    <span data-en="Active Buyer Offers & Negotiations" data-hi="खरीदार के लाइव प्रस्ताव और बातचीत">Active Buyer Offers & Negotiations</span>
                </h2>

                <div class="space-y-4">
                    <!-- Buyer Card 1 -->
                    <div class="p-4 border border-gray-200 rounded-lg hover:border-green-400 transition flex flex-col md:flex-row justify-between md:items-center gap-4">
                        <div class="flex items-start space-x-3">
                            <img src="https://images.unsplash.com/photo-1542838132-92c53300491e?w=100&h=100&fit=crop" class="w-12 h-12 rounded-full object-cover border" alt="Buyer">
                            <div>
                                <div class="flex items-center space-x-2">
                                    <h3 class="font-bold text-gray-800">Reliable Agro Traders</h3>
                                    <span class="bg-green-100 text-green-800 text-[10px] font-bold px-2 py-0.5 rounded"><i class="fa-solid fa-circle-check"></i> KYC Verified</span>
                                </div>
                                <p class="text-xs text-gray-500">Lot: Wheat (50 Qtl) • Offered: <span class="font-bold text-gray-800">₹2,420 / Qtl</span></p>
                                <p class="text-xs text-gray-400">Payment Terms: Instant UPI / NEFT on Pickup</p>
                            </div>
                        </div>

                        <div class="flex items-center space-x-2">
                            <button onclick="alert('Negotiation message sent to Reliable Agro Traders!')" class="bg-gray-100 hover:bg-gray-200 text-gray-700 px-3 py-1.5 rounded text-xs font-semibold">
                                Counter Offer
                            </button>
                            <button onclick="acceptRecommendation('Reliable Agro Traders', '₹1,21,000')" class="bg-green-600 hover:bg-green-700 text-white px-4 py-1.5 rounded text-xs font-semibold">
                                Accept Offer
                            </button>
                        </div>
                    </div>

                    <!-- Buyer Card 2 -->
                    <div class="p-4 border border-gray-200 rounded-lg hover:border-green-400 transition flex flex-col md:flex-row justify-between md:items-center gap-4">
                        <div class="flex items-start space-x-3">
                            <img src="https://images.unsplash.com/photo-1595246140625-573b715d11dc?w=100&h=100&fit=crop" class="w-12 h-12 rounded-full object-cover border" alt="Buyer">
                            <div>
                                <div class="flex items-center space-x-2">
                                    <h3 class="font-bold text-gray-800">Kissan Direct Exporters</h3>
                                    <span class="bg-green-100 text-green-800 text-[10px] font-bold px-2 py-0.5 rounded"><i class="fa-solid fa-circle-check"></i> KYC Verified</span>
                                </div>
                                <p class="text-xs text-gray-500">Lot: Wheat (50 Qtl) • Offered: <span class="font-bold text-gray-800">₹2,400 / Qtl</span></p>
                                <p class="text-xs text-gray-400">Payment Terms: 50% Advance, 50% on Delivery</p>
                            </div>
                        </div>

                        <div class="flex items-center space-x-2">
                            <button onclick="alert('Counter offer sent!')" class="bg-gray-100 hover:bg-gray-200 text-gray-700 px-3 py-1.5 rounded text-xs font-semibold">
                                Counter Offer
                            </button>
                            <button onclick="acceptRecommendation('Kissan Direct Exporters', '₹1,20,000')" class="bg-green-600 hover:bg-green-700 text-white px-4 py-1.5 rounded text-xs font-semibold">
                                Accept Offer
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ================= TAB 4: TRANSACTION & DISPUTE TRACKING ================= -->
        <section id="sec-transactions" class="space-y-6 hidden">
            <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
                <h2 class="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-clock-rotate-left text-green-600"></i>
                    <span data-en="Transaction Status & Payment Escrow" data-hi="लेनदेन की स्थिति और सुरक्षा">Transaction Status & Payment Escrow</span>
                </h2>

                <div id="active-transaction-box" class="bg-gray-50 border border-gray-200 p-4 rounded-lg">
                    <p class="text-sm text-gray-600" data-en="No confirmed deal selected yet. Create a lot or accept a buyer recommendation above." data-hi="अभी कोई सौदा चयनित नहीं है। ऊपर दिए गए विकल्पों में से चुनें।">No confirmed deal selected yet. Create a lot or accept a buyer recommendation above.</p>
                </div>

                <!-- Workflow Stepper Example -->
                <div class="mt-6 pt-6 border-t border-gray-200">
                    <h3 class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-4" data-en="Standard Transaction Workflow" data-hi="मानक कार्यप्रणाली">Standard Transaction Workflow</h3>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-center text-xs">
                        <div class="p-3 bg-green-50 rounded border border-green-200 font-semibold text-green-800">1. Lot Created & Matched</div>
                        <div class="p-3 bg-green-50 rounded border border-green-200 font-semibold text-green-800">2. Offer Accepted</div>
                        <div class="p-3 bg-yellow-50 rounded border border-yellow-200 font-semibold text-yellow-800">3. Transport & Inspection</div>
                        <div class="p-3 bg-gray-100 rounded text-gray-500">4. Escrow Payment Released</div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-gray-400 text-xs py-4 text-center mt-auto">
        <p>Smart India Hackathon 2026 • Problem Statement ID: SIH26132 • Team Mind2Matter</p>
    </footer>

    <!-- Interactive JavaScript -->
    <script>
        let currentLang = 'en';
        let selectedLotType = 'Market';

        function switchTab(tabId) {
            // Hide all sections
            document.querySelectorAll('main > section').forEach(sec => sec.classList.add('hidden'));
            
            // Remove active classes from tabs
            document.querySelectorAll('nav button').forEach(btn => {
                btn.classList.remove('active-tab');
                btn.classList.add('text-gray-600');
            });

            // Show selected section
            document.getElementById('sec-' + tabId).classList.remove('hidden');
            
            // Set active tab style
            const activeNav = document.getElementById('tab-' + tabId);
            activeNav.classList.add('active-tab');
            activeNav.classList.remove('text-gray-600');
        }

        function selectLotType(type) {
            selectedLotType = type;
            ['market', 'buyer', 'storage'].forEach(t => {
                const el = document.getElementById('lot-type-' + t);
                if (t === type.toLowerCase()) {
                    el.classList.add('border-green-500', 'bg-green-50/50');
                    el.classList.remove('border-gray-200');
                    el.querySelector('input').checked = true;
                } else {
                    el.classList.remove('border-green-500', 'bg-green-50/50');
                    el.classList.add('border-gray-200');
                    el.querySelector('input').checked = false;
                }
            });
        }

        function handleLotSubmit(event) {
            event.preventDefault();
            const crop = document.getElementById('crop-select').value;
            const qty = document.getElementById('lot-qty').value;
            const grade = document.getElementById('lot-grade').value;

            document.getElementById('rec-summary-title').innerText = 
                `Analyzing options for ${crop} (${qty} Quintals - ${grade})`;

            switchTab('recommendations');
            speakText(`Lot created successfully for ${qty} quintals of ${crop}. Showing top selling recommendations based on net profit.`);
        }

        function acceptRecommendation(entityName, profit) {
            const transBox = document.getElementById('active-transaction-box');
            transBox.innerHTML = `
                <div class="bg-green-50 border border-green-300 p-4 rounded-lg">
                    <div class="flex items-center space-x-2 text-green-800 font-bold text-md mb-2">
                        <i class="fa-solid fa-circle-check text-xl"></i>
                        <span>Deal Confirmed with ${entityName}</span>
                    </div>
                    <p class="text-xs text-gray-700">Estimated Net Payout: <span class="font-bold text-green-700">${profit}</span></p>
                    <p class="text-xs text-gray-500 mt-1">Status: Transport assigned • Digital Escrow payment held securely.</p>
                </div>
            `;
            switchTab('transactions');
            speakText(`Congratulations! Deal confirmed with ${entityName} for an estimated payout of ${profit}.`);
        }

        function switchLanguage() {
            const lang = document.getElementById('lang-select').value;
            currentLang = lang;
            document.querySelectorAll('[data-en]').forEach(el => {
                el.innerText = el.getAttribute('data-' + lang) || el.getAttribute('data-en');
            });
            document.getElementById('voice-btn-text').innerText = lang === 'hi' ? 'सुनो' : 'Listen';
        }

        function speakText(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = currentLang === 'hi' ? 'hi-IN' : 'en-US';
                utterance.rate = 0.9;
                window.speechSynthesis.speak(utterance);
            } else {
                alert('Text-to-speech is not supported in this browser.');
            }
        }

        function speakPageInfo() {
            const text = currentLang === 'hi' 
                ? 'कृषि लिंक पोर्टल में आपका स्वागत है। आप यहाँ अपने उत्पाद के लिए सही मंडी, खरीदार या गोदाम का चयन कर सकते हैं।' 
                : 'Welcome to KrishiLink Portal. You can create market, buyer, or storage lots and view personalized selling recommendations for maximum profit.';
            speakText(text);
        }
    </script>
</body>
</html>
