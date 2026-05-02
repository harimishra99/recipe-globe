"""
python manage.py seed_india

Seeds:
  - 1 Country  : India
  - 16 Regional Languages
  - 28 States + 8 UTs
  - 10 Cuisines
  - 12 Categories
  - 6 sample recipes
"""
from django.core.management.base import BaseCommand
from recipes.models import RegionalLanguage, Country, State, Cuisine, Category, Recipe, Ingredient, RecipeStep


LANGUAGES = [
    {'code':'en', 'name':'English',    'native_name':'English',      'script':'Latin'},
    {'code':'hi', 'name':'Hindi',      'native_name':'हिन्दी',         'script':'Devanagari'},
    {'code':'bn', 'name':'Bengali',    'native_name':'বাংলা',          'script':'Bengali'},
    {'code':'te', 'name':'Telugu',     'native_name':'తెలుగు',         'script':'Telugu'},
    {'code':'mr', 'name':'Marathi',    'native_name':'मराठी',          'script':'Devanagari'},
    {'code':'ta', 'name':'Tamil',      'native_name':'தமிழ்',          'script':'Tamil'},
    {'code':'gu', 'name':'Gujarati',   'native_name':'ગુજરાતી',        'script':'Gujarati'},
    {'code':'kn', 'name':'Kannada',    'native_name':'ಕನ್ನಡ',          'script':'Kannada'},
    {'code':'ml', 'name':'Malayalam',  'native_name':'മലയാളം',         'script':'Malayalam'},
    {'code':'pa', 'name':'Punjabi',    'native_name':'ਪੰਜਾਬੀ',         'script':'Gurmukhi'},
    {'code':'or', 'name':'Odia',       'native_name':'ଓଡ଼ିଆ',          'script':'Odia'},
    {'code':'as', 'name':'Assamese',   'native_name':'অসমীয়া',        'script':'Bengali'},
    {'code':'ur', 'name':'Urdu',       'native_name':'اردو',           'script':'Nastaliq'},
    {'code':'ks', 'name':'Kashmiri',   'native_name':'कॉशुर',          'script':'Devanagari'},
    {'code':'ne', 'name':'Nepali',     'native_name':'नेपाली',         'script':'Devanagari'},
    {'code':'kok','name':'Konkani',    'native_name':'कोंकणी',         'script':'Devanagari'},
]

STATES = [
    # North India
    {'name':'Uttar Pradesh',      'native':'उत्तर प्रदेश',     'code':'UP',  'region':'north',     'capital':'Lucknow',    'lang':'hi', 'extra':['ur'],
     'cuisine':'Awadhi cuisine originating from the royal kitchens of the Nawabs of Lucknow. Known for dum cooking, kebabs, biryanis and rich gravies.'},
    {'name':'Punjab',             'native':'ਪੰਜਾਬ',            'code':'PB',  'region':'north',     'capital':'Chandigarh', 'lang':'pa', 'extra':['hi'],
     'cuisine':'Robust, hearty flavours dominated by wheat, dairy, and tandoor cooking. Famous for butter chicken, dal makhani, sarson da saag and lassi.'},
    {'name':'Rajasthan',          'native':'राजस्थान',          'code':'RJ',  'region':'north',     'capital':'Jaipur',     'lang':'hi', 'extra':[],
     'cuisine':'Desert-adapted cuisine relying on preserved foods, legumes and dairy. Iconic dishes: dal baati churma, gatte ki sabzi, laal maas.'},
    {'name':'Himachal Pradesh',   'native':'हिमाचल प्रदेश',     'code':'HP',  'region':'north',     'capital':'Shimla',     'lang':'hi', 'extra':[],
     'cuisine':'Simple mountain food using local grains, legumes and forest produce. Siddu, dham, chha gosht are staples.'},
    {'name':'Uttarakhand',        'native':'उत्तराखण्ड',        'code':'UK',  'region':'north',     'capital':'Dehradun',   'lang':'hi', 'extra':[],
     'cuisine':'Pahari cuisine using mandua (finger millet), jhangora, and kafuli. Traditional recipes rooted in Garhwali and Kumaoni culture.'},
    {'name':'Haryana',            'native':'हरियाणा',            'code':'HR',  'region':'north',     'capital':'Chandigarh', 'lang':'hi', 'extra':[],
     'cuisine':'Dairy-centric simple rustic food — kachri ki sabzi, bajra khichdi, and generous use of ghee and buttermilk.'},
    {'name':'Delhi',              'native':'दिल्ली',             'code':'DL',  'region':'union',     'capital':'New Delhi',  'lang':'hi', 'extra':['ur', 'pa'],
     'cuisine':'A melting pot of Mughlai, Punjabi, Rajasthani and street food cultures. Home to chaat, chole bhature, nihari and kebabs.'},
    {'name':'Jammu & Kashmir',    'native':'जम्मू और कश्मीर',   'code':'JK',  'region':'north',     'capital':'Srinagar',   'lang':'ks', 'extra':['ur', 'hi'],
     'cuisine':'Wazwan multi-course feast culture. Rogan josh, yakhni, dum aloo and kashmiri kahwa define this rich cuisine.'},
    # South India
    {'name':'Tamil Nadu',         'native':'தமிழ்நாடு',          'code':'TN',  'region':'south',     'capital':'Chennai',    'lang':'ta', 'extra':[],
     'cuisine':'Ancient Dravidian food tradition — rice-centric, tamarind-forward, coconut-rich. Idli, dosa, sambar, rasam, and Chettinad spice blends.'},
    {'name':'Kerala',             'native':'കേരളം',               'code':'KL',  'region':'south',     'capital':'Thiruvananthapuram', 'lang':'ml', 'extra':[],
     'cuisine':'Coconut, coconut oil, and seafood define Kerala cooking. Sadya feast on banana leaf, appam with stew, fish molee, payasam.'},
    {'name':'Karnataka',          'native':'ಕರ್ನಾಟಕ',             'code':'KA',  'region':'south',     'capital':'Bengaluru',  'lang':'kn', 'extra':[],
     'cuisine':'From Udupi vegetarian tradition to Coorg meat curries. Bisi bele bath, ragi mudde, neer dosa and Mysore pak.'},
    {'name':'Andhra Pradesh',     'native':'ఆంధ్ర ప్రదేశ్',        'code':'AP',  'region':'south',     'capital':'Amaravati',  'lang':'te', 'extra':[],
     'cuisine':'One of India\'s spiciest cuisines — fiery pickles, gongura (sorrel), pesarattu, pulihora and Rayalaseema specialities.'},
    {'name':'Telangana',          'native':'తెలంగాణ',              'code':'TS',  'region':'south',     'capital':'Hyderabad',  'lang':'te', 'extra':['ur'],
     'cuisine':'Hyderabadi biryani, haleem, and mirchi bajji — Mughal meets Telugu in this cuisine known for rich Nizami heritage.'},
    {'name':'Goa',                'native':'गोंय',                 'code':'GA',  'region':'west',      'capital':'Panaji',     'lang':'kok','extra':['en'],
     'cuisine':'Portuguese-influenced coastal cuisine. Fish curries with kokum, vindaloo, xacuti, bebinca dessert and feni-soaked flavours.'},
    {'name':'Pondicherry',        'native':'புதுச்சேரி',            'code':'PY',  'region':'union',     'capital':'Puducherry', 'lang':'ta', 'extra':['en'],
     'cuisine':'French-Tamil fusion — crêpes alongside idli, baguettes with rasam. Colonial culinary heritage still alive today.'},
    # East India
    {'name':'West Bengal',        'native':'পশ্চিমবঙ্গ',            'code':'WB',  'region':'east',      'capital':'Kolkata',    'lang':'bn', 'extra':[],
     'cuisine':'Mustard-oil and fish-forward cuisine with a genius for sweets. Machher jhol, kosha mangsho, mishti doi and rasgulla.'},
    {'name':'Odisha',             'native':'ଓଡ଼ିଶା',                'code':'OD',  'region':'east',      'capital':'Bhubaneswar','lang':'or', 'extra':[],
     'cuisine':'Temple food tradition of Jagannath Puri — Mahaprasad, dalma, pakhala (fermented rice) and chenna poda sweet.'},
    {'name':'Bihar',              'native':'बिहार',                 'code':'BR',  'region':'east',      'capital':'Patna',      'lang':'hi', 'extra':[],
     'cuisine':'Simple sattvic food — litti chokha (baked wheat balls with roasted aubergine), thekua sweet and sattu sherbet.'},
    {'name':'Jharkhand',          'native':'झारखण्ड',               'code':'JH',  'region':'east',      'capital':'Ranchi',     'lang':'hi', 'extra':[],
     'cuisine':'Tribal-influenced cuisine using forest tubers, bamboo shoots, and maize. Rugra mushroom curry is a delicacy.'},
    # West India
    {'name':'Maharashtra',        'native':'महाराष्ट्र',             'code':'MH',  'region':'west',      'capital':'Mumbai',     'lang':'mr', 'extra':[],
     'cuisine':'From spicy Kolhapuri to mild Konkan seafood to Mumbai street food. Vada pav, misal pav, puran poli and sol kadhi.'},
    {'name':'Gujarat',            'native':'ગુજરાત',                'code':'GJ',  'region':'west',      'capital':'Gandhinagar','lang':'gu', 'extra':[],
     'cuisine':'Predominantly vegetarian and subtly sweet-salty. Dhokla, thepla, undhiyu, fafda and the legendary Gujarati thali.'},
    # Central India
    {'name':'Madhya Pradesh',     'native':'मध्य प्रदेश',           'code':'MP',  'region':'central',   'capital':'Bhopal',     'lang':'hi', 'extra':['ur'],
     'cuisine':'Bhopal\'s Mughlai kebabs meet Malwa\'s simple grain dishes. Dal bafla, poha with jalebi, and Indori chaat culture.'},
    {'name':'Chhattisgarh',       'native':'छत्तीसगढ़',              'code':'CG',  'region':'central',   'capital':'Raipur',     'lang':'hi', 'extra':[],
     'cuisine':'Rice-based tribal food — aamat (bamboo shoot curry), chila (rice crepes), faraa dumplings and bafauri.'},
    # Northeast India
    {'name':'Assam',              'native':'অসম',                   'code':'AS',  'region':'northeast',  'capital':'Dispur',    'lang':'as', 'extra':['bn'],
     'cuisine':'Mild, minimal-spice cuisine with fermented ingredients. Masor tenga (sour fish curry), khar and duck with lauki.'},
    {'name':'Manipur',            'native':'মণিপুর',                 'code':'MN',  'region':'northeast',  'capital':'Imphal',    'lang':'en', 'extra':[],
     'cuisine':'Fermented fish (ngari), eromba (vegetable-fish mash), and chamthong — simple, pungent and nutritious cooking.'},
    {'name':'Meghalaya',          'native':'মেঘালয়',                 'code':'ML',  'region':'northeast',  'capital':'Shillong',  'lang':'en', 'extra':[],
     'cuisine':'Jadoh (rice-pork), tungrymbai (fermented soya), dohneiiong — hearty Khasi and Jaintia tribal food.'},
    {'name':'Nagaland',           'native':'নাগাল্যান্ড',             'code':'NL',  'region':'northeast',  'capital':'Kohima',    'lang':'en', 'extra':[],
     'cuisine':'Smoked meats, axone (fermented soybean), bamboo shoot and ghost pepper — bold tribal flavours unlike anywhere else.'},
    {'name':'Sikkim',             'native':'སིལ་གུང་',               'code':'SK',  'region':'northeast',  'capital':'Gangtok',   'lang':'ne', 'extra':[],
     'cuisine':'Tibetan-Nepali blend — momo (steamed dumplings), thukpa (noodle soup), sel roti and gundruk (fermented greens).'},
    {'name':'Arunachal Pradesh',  'native':'अरुणाचल प्रदेश',        'code':'AR',  'region':'northeast',  'capital':'Itanagar',  'lang':'en', 'extra':[],
     'cuisine':'Over 26 tribes, each with unique recipes. Pika pila (bamboo shoot pickle), apong (rice beer) and thukpa are common.'},
    {'name':'Mizoram',            'native':'মিজোরাম',                'code':'MZ',  'region':'northeast',  'capital':'Aizawl',    'lang':'en', 'extra':[],
     'cuisine':'Mizo cuisine uses bamboo shoots, banana flowers and minimal spices. Bai (boiled vegetables), vawksa rep (smoked pork).'},
    {'name':'Tripura',            'native':'ত্রিপুরা',               'code':'TR',  'region':'northeast',  'capital':'Agartala',  'lang':'bn', 'extra':[],
     'cuisine':'Bengali-influenced with Borok tribal traditions — chakhwi (stew), muya (bamboo shoot) and berma (fermented fish).'},
    # Union Territories
    {'name':'Chandigarh',         'native':'ਚੰਡੀਗੜ੍ਹ',              'code':'CH',  'region':'union',     'capital':'Chandigarh', 'lang':'pa', 'extra':['hi'],
     'cuisine':'Punjabi food capital — chole kulche, butter chicken, lassi and tandoori delights.'},
    {'name':'Ladakh',             'native':'ལ་དྭགས',                 'code':'LA',  'region':'union',     'capital':'Leh',        'lang':'en', 'extra':['hi'],
     'cuisine':'High-altitude Tibetan food — tsampa (barley flour), thukpa, skyu (pasta stew) and butter tea (po cha).'},
    {'name':'Andaman & Nicobar',  'native':'अंडमान और निकोबार',     'code':'AN',  'region':'union',     'capital':'Port Blair', 'lang':'en', 'extra':['hi', 'bn'],
     'cuisine':'Tropical seafood cuisine with South Indian and Bengali influences. Coconut-based fish curries and jungle fruits.'},
    {'name':'Lakshadweep',        'native':'ലക്ഷദ്വീപ്',              'code':'LD',  'region':'union',     'capital':'Kavaratti',  'lang':'ml', 'extra':[],
     'cuisine':'Coral island food centred on tuna, coconut and rice. Mas biriyani (tuna biryani) is the signature dish.'},
]

CUISINES = [
    {'name':'Mughlai',    'desc':'Royal Mughal court cuisine — rich gravies, slow-cooked meats, aromatic biryanis and kebabs.'},
    {'name':'Chettinad', 'desc':'Fiery Tamil Nadu cuisine with 20+ whole spices, sun-dried meats and kalpasi (stone flower).'},
    {'name':'Awadhi',    'desc':'Refined Lucknow cuisine known for dum cooking — meat sealed in dough and slow-cooked over coals.'},
    {'name':'Punjabi',   'desc':'Hearty North Indian food with tandoor, generous ghee, and bold masalas.'},
    {'name':'Bengali',   'desc':'Mustard-oil, panch phoron, and fresh river fish are the pillars of this elegant cuisine.'},
    {'name':'Rajasthani','desc':'Desert-adapted cuisine using preserved ingredients, ghee and spice to combat the arid climate.'},
    {'name':'Malayali',  'desc':'Kerala\'s coconut-forward cuisine featuring appam, stew, fish molee and banana-leaf sadya.'},
    {'name':'Gujarati',  'desc':'Primarily vegetarian, sweet-salty balance, thali-based meals and delicate snacks.'},
    {'name':'Konkani',   'desc':'Coastal Goa and Karnataka cuisine — kokum, coconut milk, rice and fresh seafood.'},
    {'name':'Hyderabadi','desc':'Nawabi Nizami cuisine — dum biryani, haleem, and Mughlai-Telugu fusion.'},
]

CATEGORIES = [
    {'name':'Under 5 Minutes',   'type':'time',     'emoji':'⚡', 'icon':'fa-bolt',         'color':'#E84A4A', 'time':5,   'order':1},
    {'name':'Under 30 Minutes',  'type':'time',     'emoji':'⏱️', 'icon':'fa-clock',        'color':'#F5A623', 'time':30,  'order':2},
    {'name':'Under 1 Hour',      'type':'time',     'emoji':'🕐', 'icon':'fa-hourglass',    'color':'#4A90D9', 'time':60,  'order':3},
    {'name':'Breakfast',         'type':'meal',     'emoji':'🌅', 'icon':'fa-sun',          'color':'#FF9500', 'order':4},
    {'name':'Lunch',             'type':'meal',     'emoji':'🍱', 'icon':'fa-bowl-rice',    'color':'#5AC8FA', 'order':5},
    {'name':'Dinner',            'type':'meal',     'emoji':'🌙', 'icon':'fa-moon',         'color':'#5856D6', 'order':6},
    {'name':'Snacks & Chaat',    'type':'course',   'emoji':'🍟', 'icon':'fa-cookie',       'color':'#FF6B35', 'order':7},
    {'name':'Sweets & Desserts', 'type':'course',   'emoji':'🍮', 'icon':'fa-cake-candles', 'color':'#FF2D55', 'order':8},
    {'name':'Festival Special',  'type':'festival', 'emoji':'🎉', 'icon':'fa-star',         'color':'#FFD700', 'order':9},
    {'name':'Vegetarian',        'type':'diet',     'emoji':'🥦', 'icon':'fa-leaf',         'color':'#34C759', 'order':10},
    {'name':'Date Night',        'type':'occasion', 'emoji':'❤️', 'icon':'fa-heart',        'color':'#E8441A', 'order':11},
    {'name':'Family Feast',      'type':'occasion', 'emoji':'👨‍👩‍👧‍👦','icon':'fa-users',       'color':'#5AC8FA', 'order':12},
]

SAMPLE_RECIPES = [
    {
        'title': 'Butter Chicken (Murgh Makhani)',
        'desc':  'The world-famous creamy tomato-based chicken curry born in Delhi. Rich, mildly spiced and irresistible with naan.',
        'state': 'DL', 'cuisine': 'Mughlai', 'diet': 'nonveg', 'diff': 'medium',
        'prep': 20, 'cook': 40, 'servings': 4, 'calories': 480,
        'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800&q=80',
        'trending': True, 'featured': True, 'festival': '',
        'ingredients': [
            (4, '', 'chicken thighs, cut into pieces'), (2, 'tbsp', 'butter'),
            (1, 'cup', 'tomato puree'), (1, 'cup', 'heavy cream'),
            (2, 'tsp', 'garam masala'), (1, 'tsp', 'kashmiri red chilli powder'),
            (1, 'tbsp', 'ginger-garlic paste'), (1, 'tsp', 'sugar'), ('', '', 'salt to taste'),
        ],
        'steps': [
            (1, 'Marinate chicken in yoghurt, chilli powder, ginger-garlic paste and salt for 30 minutes.',  '', 30),
            (2, 'Grill or pan-fry the marinated chicken until charred and cooked through. Set aside.',       'For best results, use a cast iron pan.', 15),
            (3, 'Melt butter in a pan, add tomato puree and cook for 10 minutes until oil separates.',       '', 10),
            (4, 'Add garam masala, kashmiri chilli and the grilled chicken. Stir well.',                    '', 5),
            (5, 'Pour in cream, add sugar, simmer on low heat for 15 minutes. Serve with naan or rice.',    'Add kasuri methi for authentic smoky aroma.', 15),
        ],
    },
    {
        'title': 'Masala Dosa',
        'desc':  'Crispy fermented rice-lentil crepe from South India, filled with spiced potato masala. A breakfast icon.',
        'state': 'KA', 'cuisine': 'Konkani', 'diet': 'veg', 'diff': 'hard',
        'prep': 480, 'cook': 30, 'servings': 6, 'calories': 220,
        'image_url': 'https://images.unsplash.com/photo-1630383249896-424e482df921?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'ingredients': [
            (2, 'cups', 'rice'), (1, 'cup', 'urad dal'), (4, '', 'large potatoes, boiled'),
            (2, '', 'onions, sliced'), (1, 'tsp', 'mustard seeds'),
            (10, '', 'curry leaves'), (2, '', 'green chillies'), ('', '', 'salt'), ('', '', 'oil for cooking'),
        ],
        'steps': [
            (1, 'Soak rice and urad dal separately for 6 hours. Grind to smooth batter and ferment overnight.', 'Fermentation gives the sour flavour.', 480),
            (2, 'Make masala: sauté mustard seeds, curry leaves, onions, chillies. Add mashed potato, turmeric, salt.', '', 15),
            (3, 'Heat a flat tawa, pour batter in circular motion to make a thin crepe.', 'Cast iron tawa gives the best crispiness.', None),
            (4, 'Drizzle oil around edges, cook until golden and crispy on the bottom.', '', 4),
            (5, 'Place potato filling in centre, fold dosa, serve with sambar and coconut chutney.', '', None),
        ],
    },
    {
        'title': 'Litti Chokha',
        'desc':  'Bihar\'s rustic soul food — baked whole wheat dough balls filled with sattu (roasted chickpea flour), served with fire-roasted vegetable mash.',
        'state': 'BR', 'cuisine': 'Bengali', 'diet': 'veg', 'diff': 'medium',
        'prep': 30, 'cook': 40, 'servings': 4, 'calories': 310,
        'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&q=80',
        'trending': False, 'featured': True, 'festival': '',
        'ingredients': [
            (2, 'cups', 'whole wheat flour'), (1, 'cup', 'sattu (roasted gram flour)'),
            (2, '', 'brinjal (eggplant)'), (3, '', 'tomatoes'), (4, '', 'garlic cloves'),
            (2, 'tsp', 'ajwain (carom seeds)'), (2, 'tbsp', 'mustard oil'), ('', '', 'salt & green chilli'),
        ],
        'steps': [
            (1, 'Knead wheat flour with water and salt into a stiff dough. Rest 20 minutes.', '', 20),
            (2, 'Mix sattu with mustard oil, ajwain, green chilli, salt and a little water to make filling.', '', 10),
            (3, 'Roast brinjal and tomatoes directly on flame until charred. Peel and mash with garlic, mustard oil, salt — this is the chokha.', 'Char gives authentic smoky flavour.', 20),
            (4, 'Stuff dough balls with sattu filling, seal and bake over coal or in oven at 220°C for 25 minutes.', '', 25),
            (5, 'Dip hot littis in melted ghee and serve alongside chokha.', '', None),
        ],
    },
    {
        'title': 'Rogan Josh',
        'desc':  'Kashmiri slow-cooked lamb curry with whole spices and Kashmiri chillies — intense colour, deep flavour and royal heritage.',
        'state': 'JK', 'cuisine': 'Mughlai', 'diet': 'nonveg', 'diff': 'hard',
        'prep': 20, 'cook': 90, 'servings': 4, 'calories': 420,
        'image_url': 'https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=800&q=80',
        'trending': True, 'featured': True, 'festival': '',
        'ingredients': [
            (800, 'g', 'bone-in lamb pieces'), (4, '', 'kashmiri dry red chillies'),
            (4, '', 'cloves'), (2, '', 'black cardamom'), (1, 'tsp', 'fennel powder'),
            (1, 'tsp', 'dry ginger powder'), (1, 'cup', 'yoghurt, whisked'), (3, 'tbsp', 'mustard oil'),
        ],
        'steps': [
            (1, 'Heat mustard oil to smoking point, cool slightly, then fry whole spices until fragrant.', '', 5),
            (2, 'Add lamb and sear on high heat until browned on all sides.', 'Browning = flavour. Don\'t rush this step.', 15),
            (3, 'Add kashmiri chilli paste, fennel and dry ginger powder. Stir for 5 minutes.', '', 5),
            (4, 'Add whisked yoghurt one tablespoon at a time, stirring continuously to prevent curdling.', '', 10),
            (5, 'Cover and slow-cook on low heat for 60 minutes until lamb is fall-off-the-bone tender.', 'Add water if needed.', 60),
        ],
    },
    {
        'title': 'Dhokla',
        'desc':  'Gujarat\'s beloved steamed fermented chickpea-flour snack. Light, spongy and tangy — perfect for breakfast or teatime.',
        'state': 'GJ', 'cuisine': 'Gujarati', 'diet': 'veg', 'diff': 'easy',
        'prep': 120, 'cook': 20, 'servings': 6, 'calories': 180,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'ingredients': [
            (2, 'cups', 'besan (chickpea flour)'), (1, 'cup', 'sour yoghurt'),
            (1, 'tsp', 'fruit salt (eno)'), (1, 'tsp', 'turmeric'),
            (2, 'tsp', 'sugar'), (1, 'tsp', 'mustard seeds'), (10, '', 'curry leaves'),
            (2, '', 'green chillies, slit'), ('', '', 'fresh coriander and coconut to garnish'),
        ],
        'steps': [
            (1, 'Mix besan, yoghurt, turmeric, salt, sugar and water to a smooth batter. Rest 2 hours.', 'Resting improves fermentation and fluffiness.', 120),
            (2, 'Grease a steaming tray. Add eno to batter, mix quickly and pour into tray immediately.', 'Work fast after adding eno!', None),
            (3, 'Steam for 15-18 minutes until a toothpick comes out clean.', '', 18),
            (4, 'For tempering: heat oil, crackle mustard seeds, add curry leaves, chillies and a little water with sugar.', '', 5),
            (5, 'Pour tempering over dhokla, garnish with coriander and coconut. Slice and serve.', '', None),
        ],
    },
    {
        'title': 'Momo (Steamed Dumplings)',
        'desc':  'Sikkim and Darjeeling\'s soul food — delicate steamed dumplings stuffed with spiced vegetables or meat, served with fiery chilli chutney.',
        'state': 'SK', 'cuisine': 'Bengali', 'diet': 'veg', 'diff': 'medium',
        'prep': 30, 'cook': 20, 'servings': 4, 'calories': 250,
        'image_url': 'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'ingredients': [
            (2, 'cups', 'all-purpose flour'), (200, 'g', 'cabbage, finely shredded'),
            (2, '', 'onions, finely chopped'), (1, 'tbsp', 'ginger-garlic paste'),
            (2, 'tbsp', 'soy sauce'), (1, 'tsp', 'sesame oil'), ('', '', 'salt and pepper'),
            (4, '', 'dried red chillies (for chutney)'), (4, '', 'tomatoes (for chutney)'),
        ],
        'steps': [
            (1, 'Knead flour with water to a smooth, stiff dough. Cover and rest 20 minutes.', '', 20),
            (2, 'Mix shredded cabbage, onion, ginger-garlic, soy sauce, sesame oil, salt, pepper to make filling.', '', 10),
            (3, 'Roll dough thin, cut circles, place filling in centre, pleat and seal into half-moon or round shapes.', 'Keep dough covered to prevent drying.', None),
            (4, 'Steam in a greased steamer basket for 12-15 minutes until translucent.', '', 15),
            (5, 'For chutney: roast chillies and tomatoes, blend with garlic and salt. Serve alongside hot momos.', '', 5),
        ],
    },
]


class Command(BaseCommand):
    help = 'Seed India-specific data into RecipeGlobe'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('🌏 Seeding RecipeGlobe India data...'))

        # Languages
        lang_map = {}
        for l in LANGUAGES:
            obj, c = RegionalLanguage.objects.get_or_create(code=l['code'], defaults=l)
            lang_map[l['code']] = obj
        self.stdout.write(f'  ✅ {len(lang_map)} languages')

        # Country
        india, _ = Country.objects.get_or_create(
            code='IND',
            defaults={'name':'India','flag_emoji':'🇮🇳','default_language':lang_map['hi'],'is_active':True,
                      'description':'A land of 28 states and 8 union territories with the world\'s most diverse culinary traditions.'}
        )
        self.stdout.write('  ✅ Country: India')

        # States
        state_map = {}
        for s in STATES:
            pl = lang_map.get(s['lang'])
            obj, c = State.objects.get_or_create(
                code=s['code'],
                defaults={
                    'country': india, 'name': s['name'], 'native_name': s['native'],
                    'capital': s['capital'], 'region': s['region'],
                    'primary_language': pl,
                    'cuisine_summary': s['cuisine'], 'is_active': True,
                }
            )
            for ex in s.get('extra', []):
                if ex in lang_map:
                    obj.additional_languages.add(lang_map[ex])
            state_map[s['code']] = obj
        self.stdout.write(f'  ✅ {len(state_map)} states & UTs')

        # Cuisines
        cuisine_map = {}
        for c in CUISINES:
            obj, _ = Cuisine.objects.get_or_create(name=c['name'], defaults={'description':c['desc'],'is_active':True})
            cuisine_map[c['name']] = obj
        self.stdout.write(f'  ✅ {len(cuisine_map)} cuisines')

        # Categories
        cat_map = {}
        for c in CATEGORIES:
            obj, _ = Category.objects.get_or_create(
                name=c['name'],
                defaults={'category_type':c['type'],'emoji':c.get('emoji',''),'icon':c.get('icon',''),
                          'color':c['color'],'max_time_minutes':c.get('time'),'order':c['order']}
            )
            cat_map[c['name']] = obj
        self.stdout.write(f'  ✅ {len(cat_map)} categories')

        # Recipes
        from django.contrib.auth.models import User
        admin_user = User.objects.filter(is_superuser=True).first()

        for r in SAMPLE_RECIPES:
            if Recipe.objects.filter(title=r['title']).exists():
                continue
            state   = state_map.get(r['state'])
            cuisine = cuisine_map.get(r['cuisine'])
            recipe  = Recipe.objects.create(
                title=r['title'], description=r['desc'],
                country=india, state=state, cuisine=cuisine,
                diet_type=r['diet'], difficulty=r['diff'],
                prep_time=r['prep'], cook_time=r['cook'],
                servings=r['servings'], calories_per_serving=r['calories'],
                image_url=r['image_url'], is_trending=r['trending'],
                is_featured=r['featured'], festival_tag=r['festival'],
                is_published=True, author=admin_user,
            )
            for i, (qty, unit, name) in enumerate(r['ingredients'], 1):
                Ingredient.objects.create(recipe=recipe, quantity=str(qty), unit=unit, name=name, order=i)
            for step_num, instruction, tip, time_min in r['steps']:
                RecipeStep.objects.create(
                    recipe=recipe, step_number=step_num,
                    instruction=instruction, tip=tip or '',
                    time_minutes=time_min,
                )
        self.stdout.write(f'  ✅ {len(SAMPLE_RECIPES)} sample recipes')
        self.stdout.write(self.style.SUCCESS('\n🎉 India seed complete! Run: python manage.py createsuperuser'))
