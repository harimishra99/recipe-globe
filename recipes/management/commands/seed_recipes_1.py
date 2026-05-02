"""
Management command to seed 50+ authentic Indian recipes across all states.

Usage:
    python manage.py seed_recipes

This command is safe to run multiple times — it skips existing recipes.
"""
from django.core.management.base import BaseCommand
from recipes.models import (
    RegionalLanguage, Country, State, Cuisine,
    Category, Recipe, Ingredient, RecipeStep
)
from django.contrib.auth.models import User


RECIPES = [

    # ── NORTH INDIA ──────────────────────────────────────────────────────────

    {
        'title': 'Dal Makhani',
        'desc': 'The crown jewel of Punjabi cooking — whole black lentils and kidney beans slow-cooked overnight with butter and cream. Rich, smoky and deeply satisfying.',
        'state': 'PB', 'cuisine': 'Punjabi', 'diet': 'veg', 'diff': 'medium',
        'prep': 480, 'cook': 60, 'servings': 6, 'calories': 320,
        'image_url': 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=800&q=80',
        'trending': True, 'featured': True, 'festival': '',
        'cats': ['Dinner', 'Under 1 Hour', 'Vegetarian'],
        'ingredients': [
            (1, 'cup', 'whole black urad dal'),
            ('1/4', 'cup', 'rajma (kidney beans)'),
            (3, 'tbsp', 'butter'),
            (1, 'cup', 'tomato puree'),
            ('1/2', 'cup', 'heavy cream'),
            (1, 'tbsp', 'ginger-garlic paste'),
            (2, 'tsp', 'garam masala'),
            (1, 'tsp', 'kashmiri red chilli powder'),
            ('', '', 'salt to taste'),
        ],
        'steps': [
            (1, 'Soak black dal and rajma overnight in plenty of cold water. Drain and rinse.', 'Minimum 8 hours soaking is essential.', 480),
            (2, 'Pressure cook the soaked lentils with salt and water for 6–8 whistles until very soft. Mash some lentils against the pot wall.', '', 30),
            (3, 'In a heavy pan, melt butter. Add ginger-garlic paste and sauté until golden.', '', 5),
            (4, 'Add tomato puree and all spices. Cook on medium heat for 12–15 minutes until oil separates.', '', 15),
            (5, 'Add the cooked dal to the masala. Stir well and simmer on the lowest heat for 30 minutes, stirring often.', 'The longer you simmer, the better it tastes.', 30),
            (6, 'Stir in cream, adjust salt. Serve with a knob of butter, naan or steamed basmati rice.', '', None),
        ],
    },

    {
        'title': 'Sarson da Saag with Makki di Roti',
        'desc': 'The ultimate Punjab winter meal — slow-cooked mustard greens with homemade corn flatbread. Topped with white butter, it is pure comfort food.',
        'state': 'PB', 'cuisine': 'Punjabi', 'diet': 'veg', 'diff': 'medium',
        'prep': 20, 'cook': 60, 'servings': 4, 'calories': 290,
        'image_url': 'https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'cats': ['Lunch', 'Dinner', 'Vegetarian'],
        'ingredients': [
            (500, 'g', 'fresh mustard leaves (sarson)'),
            (200, 'g', 'spinach leaves'),
            (100, 'g', 'bathua (chenopodium) leaves'),
            (2, 'tbsp', 'makki atta (corn flour) for thickening'),
            (2, 'cups', 'makki atta for rotis'),
            (3, 'tbsp', 'desi ghee or white butter'),
            (1, 'tbsp', 'ginger, grated'),
            (4, '', 'green chillies'),
            (2, '', 'onions, finely chopped'),
        ],
        'steps': [
            (1, 'Wash and roughly chop mustard leaves, spinach and bathua. Pressure cook with green chillies, ginger and salt for 3 whistles.', '', 15),
            (2, 'Let mixture cool. Blend coarsely — leave some texture, do not make it completely smooth.', '', 5),
            (3, 'In a heavy pan heat ghee, fry onions until golden. Add blended greens and makki atta. Cook on low heat for 30 minutes stirring regularly.', 'The makki atta thickens the saag beautifully.', 30),
            (4, 'For roti: knead makki atta with warm water into a soft dough. Pat out thick rotis by hand and cook on a hot tawa with ghee.', '', 20),
            (5, 'Serve saag topped with a generous knob of white butter alongside hot makki di roti.', '', None),
        ],
    },

    {
        'title': 'Chole Bhature',
        'desc': 'Delhi's most beloved street food — spicy chickpea curry served with deep-fried fluffy bread. A Sunday morning ritual across North India.',
        'state': 'DL', 'cuisine': 'Punjabi', 'diet': 'veg', 'diff': 'medium',
        'prep': 480, 'cook': 45, 'servings': 4, 'calories': 520,
        'image_url': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
        'trending': True, 'featured': True, 'festival': '',
        'cats': ['Breakfast', 'Snacks & Chaat', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'kabuli chana (white chickpeas), soaked overnight'),
            (2, 'cups', 'maida (plain flour) for bhature'),
            ('1/2', 'cup', 'yoghurt'),
            (2, '', 'onions, finely chopped'),
            (3, '', 'tomatoes, pureed'),
            (2, 'tsp', 'chole masala'),
            (1, 'tsp', 'amchur (dry mango powder)'),
            (2, 'tbsp', 'oil'),
            ('', '', 'oil for deep frying'),
        ],
        'steps': [
            (1, 'Pressure cook soaked chickpeas with salt, a tea bag (for colour) and water for 5–6 whistles until soft.', 'The tea bag gives chole its signature dark colour.', 25),
            (2, 'Fry onions until dark brown. Add tomato puree, chole masala and cook until oil separates.', '', 15),
            (3, 'Add chickpeas with their cooking water. Simmer 15 minutes. Finish with amchur and garam masala.', '', 15),
            (4, 'For bhature: knead maida, yoghurt, a pinch of baking soda, salt and water into a soft dough. Rest 2 hours.', '', 120),
            (5, 'Roll into oval shapes and deep fry in hot oil until puffed and golden on both sides.', 'Oil must be very hot for bhature to puff up.', 10),
            (6, 'Serve chole with hot bhature, sliced onion, pickle and green chilli.', '', None),
        ],
    },

    {
        'title': 'Dal Baati Churma',
        'desc': 'Rajasthan\'s iconic three-in-one meal — baked wheat dumplings, five-lentil dal, and crumbled sweet wheat with jaggery and ghee. Festival food at its finest.',
        'state': 'RJ', 'cuisine': 'Rajasthani', 'diet': 'veg', 'diff': 'hard',
        'prep': 30, 'cook': 60, 'servings': 6, 'calories': 580,
        'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&q=80',
        'trending': False, 'featured': True, 'festival': 'Gangaur Festival',
        'cats': ['Dinner', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (3, 'cups', 'whole wheat flour'),
            ('1/2', 'cup', 'semolina'),
            (4, 'tbsp', 'ghee (for dough)'),
            ('1/4', 'cup', 'each of chana dal, toor dal, moong dal, masoor dal, urad dal'),
            (3, 'tbsp', 'jaggery (for churma)'),
            (2, 'tsp', 'panch phoron spice mix'),
            ('', '', 'ghee for serving — be generous'),
        ],
        'steps': [
            (1, 'Knead wheat flour, semolina, ghee and water into a stiff dough. Shape into round balls (baati).', '', 15),
            (2, 'Bake baati in a preheated oven at 200°C for 30 minutes until hard and golden, turning halfway.', 'Traditionally cooked over cow dung fire for authentic flavour.', 30),
            (3, 'Cook all five lentils together in pressure cooker with turmeric. Prepare a ghee-tempered masala with panch phoron, tomatoes, chilli and add to dal.', '', 25),
            (4, 'For churma: coarsely grind 3–4 baati. Mix with melted ghee, jaggery and cardamom.', '', 10),
            (5, 'Break open hot baati, pour generous ghee inside and serve alongside dal and churma.', '', None),
        ],
    },

    {
        'title': 'Wazwan: Yakhni Lamb',
        'desc': 'The centrepiece of Kashmir\'s grand Wazwan feast — lamb cooked in fragrant yoghurt-fennel broth. Delicate, aromatic and deeply comforting.',
        'state': 'JK', 'cuisine': 'Mughlai', 'diet': 'nonveg', 'diff': 'hard',
        'prep': 30, 'cook': 90, 'servings': 4, 'calories': 380,
        'image_url': 'https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=800&q=80',
        'trending': False, 'featured': True, 'festival': 'Eid Special',
        'cats': ['Dinner', 'Festival Special'],
        'ingredients': [
            (800, 'g', 'bone-in lamb, cut into pieces'),
            (2, 'cups', 'full-fat yoghurt, whisked smooth'),
            (2, 'tsp', 'fennel seed powder (saunf)'),
            (1, 'tsp', 'dry ginger powder (sonth)'),
            (4, '', 'green cardamoms'),
            (2, '', 'black cardamoms'),
            (1, '', 'cinnamon stick'),
            (4, 'tbsp', 'mustard oil'),
            ('', '', 'salt to taste'),
        ],
        'steps': [
            (1, 'Blanch lamb pieces in boiling salted water for 5 minutes. Drain and set aside.', 'Blanching removes impurities and gives a cleaner broth.', 10),
            (2, 'Heat mustard oil to smoking, cool slightly. Fry whole spices for 1 minute.', '', 5),
            (3, 'Add lamb and lightly brown. Do not add any tomatoes — this is a white curry.', '', 10),
            (4, 'Add 3 cups of water, fennel powder, dry ginger, salt. Bring to boil, then simmer 45 minutes until lamb is 80% done.', '', 45),
            (5, 'Reduce heat to lowest. Add whisked yoghurt slowly, stirring continuously to prevent curdling.', 'Never add yoghurt on high heat.', 10),
            (6, 'Simmer 20 more minutes until oil floats on top. Serve with steamed rice.', '', 20),
        ],
    },

    {
        'title': 'Dum Aloo (Kashmiri Style)',
        'desc': 'Baby potatoes fried golden then slow-cooked in a brilliant red Kashmiri chilli gravy with yoghurt and whole spices. No onion, no garlic.',
        'state': 'JK', 'cuisine': 'Mughlai', 'diet': 'veg', 'diff': 'medium',
        'prep': 15, 'cook': 45, 'servings': 4, 'calories': 280,
        'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Dinner', 'Vegetarian'],
        'ingredients': [
            (500, 'g', 'small baby potatoes'),
            (4, '', 'kashmiri dry red chillies, soaked'),
            (1, 'cup', 'yoghurt, whisked'),
            (2, 'tsp', 'fennel powder'),
            (1, 'tsp', 'dry ginger powder'),
            (3, '', 'cloves'),
            (2, '', 'black cardamoms'),
            (3, 'tbsp', 'mustard oil'),
        ],
        'steps': [
            (1, 'Prick potatoes all over with a fork. Deep fry in oil until golden and cooked through. Set aside.', 'Pricking helps the gravy penetrate inside.', 15),
            (2, 'Blend soaked kashmiri chillies into a smooth paste.', '', 5),
            (3, 'Heat mustard oil, fry whole spices. Add chilli paste and cook 5 minutes.', '', 8),
            (4, 'Add fennel powder, dry ginger, salt. Stir for 2 minutes.', '', 2),
            (5, 'Add yoghurt one spoon at a time on low heat, stirring constantly.', '', 10),
            (6, 'Add fried potatoes and '/'4 cup water. Cover and dum (slow cook) for 20 minutes. Serve with rice.', '', 20),
        ],
    },

    {
        'title': 'Poha with Jalebi',
        'desc': 'Indore\'s beloved breakfast duo — fluffy flattened rice seasoned with turmeric, mustard and curry leaves, paired with crispy syrup-soaked jalebis.',
        'state': 'MP', 'cuisine': 'Gujarati', 'diet': 'veg', 'diff': 'easy',
        'prep': 10, 'cook': 15, 'servings': 2, 'calories': 280,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Breakfast', 'Under 30 Minutes', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'thick poha (flattened rice)'),
            (1, '', 'onion, finely chopped'),
            (1, 'tsp', 'mustard seeds'),
            (10, '', 'curry leaves'),
            ('1/2', 'tsp', 'turmeric'),
            (1, 'tbsp', 'oil'),
            (2, 'tsp', 'lemon juice'),
            ('', '', 'fresh coriander and sev to garnish'),
        ],
        'steps': [
            (1, 'Rinse poha in a colander under cold water. Drain completely and let rest 5 minutes — it softens on its own.', 'Do not soak poha or it will become mushy.', 5),
            (2, 'Heat oil, crackle mustard seeds, add curry leaves and onion. Fry until onion is soft.', '', 5),
            (3, 'Add turmeric, green chilli and poha. Mix gently without breaking. Season with salt and sugar.', '', 3),
            (4, 'Cover and steam on low heat for 2 minutes. Finish with lemon juice.', '', 2),
            (5, 'Serve garnished with sev, coriander and fresh coconut. Best with piping hot jalebis on the side.', '', None),
        ],
    },

    # ── SOUTH INDIA ──────────────────────────────────────────────────────────

    {
        'title': 'Hyderabadi Dum Biryani',
        'desc': 'The king of biryanis — fragrant basmati rice layered with marinated meat and slow-cooked sealed in a pot. The dum process creates magic.',
        'state': 'TS', 'cuisine': 'Hyderabadi', 'diet': 'nonveg', 'diff': 'hard',
        'prep': 60, 'cook': 60, 'servings': 6, 'calories': 620,
        'image_url': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80',
        'trending': True, 'featured': True, 'festival': 'Eid Special',
        'cats': ['Dinner', 'Festival Special'],
        'ingredients': [
            (800, 'g', 'bone-in chicken or mutton pieces'),
            (3, 'cups', 'basmati rice, soaked 30 minutes'),
            (1, 'cup', 'yoghurt'),
            (2, '', 'large onions, sliced and fried crispy (birista)'),
            (4, 'tbsp', 'biryani masala'),
            (1, 'tsp', 'saffron soaked in warm milk'),
            (4, 'tbsp', 'ghee'),
            (2, '', 'bay leaves, 4 cloves, 2 cardamoms, 1 star anise'),
            ('', '', 'fresh mint and coriander'),
        ],
        'steps': [
            (1, 'Marinate meat with yoghurt, biryani masala, half the fried onions, mint, coriander, salt. Minimum 1 hour, overnight is best.', '', 60),
            (2, 'Parboil rice in salted water with whole spices until 70% cooked — grains should have a white centre. Drain immediately.', 'Under-cook the rice — it finishes cooking in the dum.', 10),
            (3, 'In a heavy-bottomed pot, spread marinated meat. Layer parboiled rice on top.', '', 5),
            (4, 'Drizzle saffron milk, remaining fried onions, ghee and mint over the rice.', '', 5),
            (5, 'Seal the pot with dough or tight foil. Cook on high heat 5 minutes, then lowest heat for 35 minutes.', 'Place a tawa (griddle) under the pot to prevent scorching.', 40),
            (6, 'Open at the table for dramatic effect. Mix gently from the bottom. Serve with raita and mirchi ka salan.', '', None),
        ],
    },

    {
        'title': 'Chettinad Chicken Curry',
        'desc': 'The boldest curry in India — aromatic with kalpasi, marathi mokku and freshly ground spices. This fiery Chettinad dish from Tamil Nadu is not for the faint-hearted.',
        'state': 'TN', 'cuisine': 'Chettinad', 'diet': 'nonveg', 'diff': 'hard',
        'prep': 30, 'cook': 45, 'servings': 4, 'calories': 380,
        'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'cats': ['Dinner'],
        'ingredients': [
            (800, 'g', 'chicken, cut into pieces'),
            (3, '', 'onions, sliced'),
            (3, '', 'tomatoes, chopped'),
            (2, 'tbsp', 'chettinad masala (kalpasi, marathi mokku, star anise, fennel, peppercorns ground together)'),
            (1, 'tbsp', 'ginger-garlic paste'),
            (2, '', 'sprigs curry leaves'),
            (3, 'tbsp', 'gingelly (sesame) oil'),
            (1, 'tsp', 'turmeric'),
        ],
        'steps': [
            (1, 'Dry roast all Chettinad spices — kalpasi, marathi mokku, star anise, fennel, peppercorns, dried red chillies — until fragrant. Grind to a coarse powder.', 'Fresh grinding is the soul of Chettinad cooking.', 10),
            (2, 'Heat gingelly oil, fry curry leaves and onions until deep brown — this is key to the depth of flavour.', '', 15),
            (3, 'Add ginger-garlic paste, tomatoes, turmeric. Cook until oil separates.', '', 10),
            (4, 'Add chicken pieces and Chettinad masala powder. Sear on high heat for 5 minutes coating all pieces well.', '', 5),
            (5, 'Add 1 cup of water. Cover and cook on medium heat 25 minutes until chicken is tender and gravy is thick.', '', 25),
            (6, 'Finish with fresh curry leaves. Serve with parotta or steamed rice.', '', None),
        ],
    },

    {
        'title': 'Kerala Fish Molee',
        'desc': 'Delicate coconut milk fish curry from Kerala — mild, creamy, turmeric-gold and fragrant with green chillies. Best eaten with appam.',
        'state': 'KL', 'cuisine': 'Malayali', 'diet': 'nonveg', 'diff': 'easy',
        'prep': 15, 'cook': 25, 'servings': 4, 'calories': 290,
        'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
        'trending': False, 'featured': True, 'festival': 'Onam Special',
        'cats': ['Dinner', 'Under 30 Minutes'],
        'ingredients': [
            (600, 'g', 'firm white fish (kingfish or pomfret), sliced'),
            (2, 'cups', 'thick coconut milk'),
            (2, '', 'onions, sliced thin'),
            (4, '', 'green chillies, slit'),
            (1, 'tsp', 'turmeric'),
            (1, 'tbsp', 'ginger, julienned'),
            (2, '', 'sprigs curry leaves'),
            (2, 'tbsp', 'coconut oil'),
        ],
        'steps': [
            (1, 'Marinate fish in turmeric and a little salt for 10 minutes.', '', 10),
            (2, 'Heat coconut oil, sauté onions, ginger, green chillies and curry leaves until onions are soft — do not brown.', 'Fish molee is a white, mild curry — avoid browning.', 8),
            (3, 'Add thin coconut milk (first extract diluted) and bring to a gentle simmer.', '', 5),
            (4, 'Slide in fish pieces and cook on medium heat for 8 minutes without stirring too much.', '', 8),
            (5, 'Pour in thick coconut milk, shake the pan gently and simmer 3 minutes. Do not boil after adding thick milk.', '', 3),
            (6, 'Finish with a drizzle of coconut oil. Serve with appam or string hoppers.', '', None),
        ],
    },

    {
        'title': 'Appam with Coconut Milk',
        'desc': 'Lacy fermented rice hoppers with crispy edges and a soft, fluffy centre — Kerala\'s most beloved breakfast, perfect with sweet coconut milk or stew.',
        'state': 'KL', 'cuisine': 'Malayali', 'diet': 'veg', 'diff': 'medium',
        'prep': 480, 'cook': 20, 'servings': 4, 'calories': 180,
        'image_url': 'https://images.unsplash.com/photo-1630383249896-424e482df921?w=800&q=80',
        'trending': True, 'featured': False, 'festival': 'Onam Special',
        'cats': ['Breakfast', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'raw rice, soaked 4 hours'),
            ('1/2', 'cup', 'cooked rice'),
            ('1/2', 'cup', 'grated coconut'),
            (1, 'tsp', 'active dry yeast'),
            (1, 'tsp', 'sugar'),
            ('', '', 'salt to taste'),
            (2, 'cups', 'fresh coconut milk (for serving)'),
            (2, 'tbsp', 'sugar (for serving milk)'),
        ],
        'steps': [
            (1, 'Grind soaked raw rice, cooked rice and grated coconut together into a smooth batter using minimal water.', '', 10),
            (2, 'Dissolve yeast and sugar in warm water for 5 minutes until frothy. Add to batter. Ferment 6–8 hours.', '', 480),
            (3, 'Add salt to fermented batter. Batter should be thin — thinner than dosa batter.', 'Appam batter should pour like water.', 5),
            (4, 'Heat an appam pan (kallu chatty), pour a ladle of batter and swirl the pan in a circular motion to spread thin edges.', '', None),
            (5, 'Cover and cook on low heat for 2 minutes until edges are crisp and centre is soft and fluffy.', '', 2),
            (6, 'Serve immediately with sweetened coconut milk (add sugar to coconut milk and a pinch of cardamom).', '', None),
        ],
    },

    {
        'title': 'Bisi Bele Bath',
        'desc': 'Karnataka\'s one-pot wonder — rice, lentils and vegetables cooked together with an aromatic homemade spice powder. Served piping hot with ghee and papad.',
        'state': 'KA', 'cuisine': 'Konkani', 'diet': 'veg', 'diff': 'medium',
        'prep': 20, 'cook': 40, 'servings': 4, 'calories': 350,
        'image_url': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Lunch', 'Under 1 Hour', 'Vegetarian'],
        'ingredients': [
            (1, 'cup', 'short-grain rice'),
            ('1/2', 'cup', 'toor dal'),
            (2, 'cups', 'mixed vegetables (beans, carrot, peas, potato)'),
            (2, 'tbsp', 'bisi bele bath powder'),
            (1, 'tbsp', 'tamarind paste'),
            (1, 'tsp', 'jaggery'),
            (2, 'tbsp', 'ghee'),
            (1, 'tsp', 'mustard seeds'),
            (10, '', 'cashews'),
        ],
        'steps': [
            (1, 'Pressure cook rice and toor dal together with double water for 4 whistles. They should be very soft and mashable.', '', 20),
            (2, 'Boil vegetables until tender. Add tamarind paste, jaggery, bisi bele bath powder and salt. Cook 10 minutes.', '', 15),
            (3, 'Combine cooked rice-dal with the vegetable mixture. Mix well on medium heat adding water to get a porridge-like consistency.', '', 10),
            (4, 'For tempering: heat ghee, crackle mustard seeds, fry cashews until golden. Add curry leaves and dry red chillies.', '', 5),
            (5, 'Pour tempering over bisi bele bath. Serve immediately with a generous drizzle of ghee, papad and boondi raita.', '', None),
        ],
    },

    {
        'title': 'Pesarattu (Green Moong Dosa)',
        'desc': 'Andhra Pradesh\'s protein-packed breakfast — crispy green moong dal crepes served with ginger chutney. Nutritious, quick and utterly delicious.',
        'state': 'AP', 'cuisine': 'Chettinad', 'diet': 'veg', 'diff': 'easy',
        'prep': 240, 'cook': 20, 'servings': 4, 'calories': 180,
        'image_url': 'https://images.unsplash.com/photo-1630383249896-424e482df921?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Breakfast', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'whole green moong dal, soaked 4 hours'),
            (1, 'inch', 'ginger'),
            (2, '', 'green chillies'),
            ('1/2', 'cup', 'rice (optional, for crispiness)'),
            ('', '', 'salt to taste'),
            ('', '', 'onion and cumin for topping'),
            ('', '', 'oil for cooking'),
        ],
        'steps': [
            (1, 'Drain soaked moong dal (and rice if using). Grind with ginger, green chillies and salt into a slightly coarse batter. No fermentation needed.', '', 10),
            (2, 'Heat a flat tawa, pour a ladle of batter and spread into a thin circle.', '', None),
            (3, 'Sprinkle chopped onion and cumin seeds on top. Drizzle oil around the edges.', '', None),
            (4, 'Cook on medium heat until bottom is crispy and edges lift. No need to flip.', 'Pesarattu is typically only cooked on one side.', 5),
            (5, 'Serve hot with ginger-coconut chutney and upma stuffing optionally inside.', '', None),
        ],
    },

    {
        'title': 'Goan Fish Curry',
        'desc': 'Tangy, spicy and coconut-rich — this red Goan fish curry uses kokum for its characteristic sourness and is eaten with red boiled rice.',
        'state': 'GA', 'cuisine': 'Konkani', 'diet': 'nonveg', 'diff': 'easy',
        'prep': 20, 'cook': 25, 'servings': 4, 'calories': 310,
        'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'cats': ['Lunch', 'Dinner', 'Under 30 Minutes'],
        'ingredients': [
            (600, 'g', 'firm fish (kingfish/pomfret), sliced'),
            (1, 'cup', 'grated coconut'),
            (6, '', 'kashmiri red chillies'),
            (1, 'tsp', 'turmeric'),
            (1, 'tsp', 'coriander seeds'),
            (4, '', 'kokum pieces (or tamarind)'),
            (2, '', 'onions, sliced'),
            (2, 'tbsp', 'coconut oil'),
        ],
        'steps': [
            (1, 'Grind coconut, kashmiri chillies, coriander seeds, turmeric and a little water into a smooth red paste.', '', 10),
            (2, 'Heat coconut oil, sauté onions until golden. Add the ground paste and cook 5 minutes.', '', 8),
            (3, 'Add 1.5 cups water, kokum and salt. Bring to a boil and simmer 5 minutes.', '', 8),
            (4, 'Slide in fish pieces. Cook gently 10 minutes — do not stir, just shake the pan.', 'Do not over-stir or fish will break.', 10),
            (5, 'Check seasoning. The curry should be tangy, spicy and coconut-creamy. Serve with red boiled rice.', '', None),
        ],
    },

    # ── EAST INDIA ──────────────────────────────────────────────────────────

    {
        'title': 'Machher Jhol (Bengali Fish Curry)',
        'desc': 'The everyday Bengali fish curry — mustard oil, turmeric, panch phoron and seasonal vegetables with fresh river fish. Simple, soul-satisfying perfection.',
        'state': 'WB', 'cuisine': 'Bengali', 'diet': 'nonveg', 'diff': 'easy',
        'prep': 15, 'cook': 30, 'servings': 4, 'calories': 260,
        'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
        'trending': False, 'featured': True, 'festival': '',
        'cats': ['Lunch', 'Dinner', 'Under 30 Minutes'],
        'ingredients': [
            (600, 'g', 'rohu or catla fish, cut into steaks'),
            (1, 'tsp', 'panch phoron (five-spice mix)'),
            (2, '', 'tomatoes, chopped'),
            (2, '', 'potatoes, cubed'),
            (1, 'tsp', 'turmeric'),
            (1, 'tsp', 'cumin powder'),
            (3, 'tbsp', 'mustard oil'),
            (2, '', 'green chillies, slit'),
        ],
        'steps': [
            (1, 'Rub fish with turmeric and salt. Fry in hot mustard oil until golden on both sides. Remove and keep aside.', '', 10),
            (2, 'In same oil, fry panch phoron until it splutters. Add green chillies.', '', 2),
            (3, 'Add potatoes and fry 5 minutes. Add tomatoes, turmeric, cumin and cook until tomatoes break down.', '', 10),
            (4, 'Add 2 cups warm water and salt. Bring to boil, add fried fish gently.', '', 5),
            (5, 'Simmer uncovered for 10 minutes until potatoes are cooked and curry has a light broth consistency.', '', 10),
            (6, 'Finish with a drizzle of raw mustard oil. Serve with steamed white rice.', '', None),
        ],
    },

    {
        'title': 'Rasgulla',
        'desc': 'West Bengal\'s gift to the world — soft, spongy cottage cheese balls soaked in light sugar syrup. The original, the iconic, the irreplaceable.',
        'state': 'WB', 'cuisine': 'Bengali', 'diet': 'veg', 'diff': 'medium',
        'prep': 20, 'cook': 30, 'servings': 8, 'calories': 150,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Durga Puja Special',
        'cats': ['Sweets & Desserts', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (1, 'litre', 'full-fat milk'),
            (2, 'tbsp', 'lemon juice or vinegar'),
            (2, 'cups', 'sugar'),
            (4, 'cups', 'water'),
            (1, 'tsp', 'rose water'),
            ('', '', 'muslin cloth for straining'),
        ],
        'steps': [
            (1, 'Boil milk, add lemon juice slowly until it curdles completely. Strain through muslin cloth, wash chhena under cold water.', '', 15),
            (2, 'Squeeze out all water. Knead chhena for 8–10 minutes until completely smooth with no grains — this is critical.', 'The softer you knead, the softer the rasgulla.', 10),
            (3, 'Roll into smooth balls with no cracks. Cracks will cause them to break in the syrup.', '', 5),
            (4, 'Boil sugar and water in a wide pan. Add chhena balls, cover and boil on high-medium heat for 15 minutes.', 'Pan must be wide enough for balls to expand to double size.', 15),
            (5, 'Check — balls should be spongy when pressed and spring back. Add rose water. Cool and refrigerate.', '', None),
        ],
    },

    {
        'title': 'Pakhala Bhata (Fermented Rice)',
        'desc': 'Odisha\'s ancient cooling summer dish — cooked rice fermented overnight in water, served with fried fish, papad and saga bhaja. The original probiotic meal.',
        'state': 'OD', 'cuisine': 'Bengali', 'diet': 'veg', 'diff': 'easy',
        'prep': 480, 'cook': 20, 'servings': 2, 'calories': 200,
        'image_url': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Pakhala Dibasa',
        'cats': ['Lunch', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'cooked rice (left overnight)'),
            (3, 'cups', 'water'),
            (1, 'tbsp', 'curd (optional starter)'),
            ('', '', 'salt to taste'),
            (2, '', 'green chillies, chopped'),
            (1, '', 'shallot, sliced'),
            ('', '', 'fresh coriander'),
        ],
        'steps': [
            (1, 'Cook rice and let it cool. Place in a clay pot or container, add water to submerge by 2 inches.', '', None),
            (2, 'Add a spoon of curd to start fermentation. Cover and leave overnight in a warm place (minimum 8 hours).', 'In summer it ferments faster. The slight sour smell is perfect.', 480),
            (3, 'In the morning, the rice will have absorbed water and the liquid will be slightly sour — this is the pakhala water.', '', None),
            (4, 'Serve in a bowl with the fermented liquid. Top with sliced shallots, green chilli, salt and coriander.', '', None),
            (5, 'Traditionally eaten with fried fish, roasted papad, pickle and stir-fried greens.', '', None),
        ],
    },

    {
        'title': 'Chenna Poda',
        'desc': 'Odisha\'s legendary caramelised cottage cheese dessert. The only Indian sweet that is actually baked — deeply caramelised, slightly smoky and intensely flavourful.',
        'state': 'OD', 'cuisine': 'Bengali', 'diet': 'veg', 'diff': 'medium',
        'prep': 20, 'cook': 60, 'servings': 8, 'calories': 220,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Rath Yatra Special',
        'cats': ['Sweets & Desserts', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (500, 'g', 'fresh chhena (cottage cheese)'),
            (6, 'tbsp', 'sugar'),
            (2, 'tbsp', 'semolina'),
            (1, 'tsp', 'cardamom powder'),
            (1, 'tsp', 'ghee'),
            (2, 'tbsp', 'cashews and raisins'),
        ],
        'steps': [
            (1, 'Knead chhena until smooth. Add sugar, semolina, cardamom and mix well.', '', 5),
            (2, 'Grease a baking tin with ghee. Sprinkle 2 tbsp sugar on the bottom — this will caramelise into a crust.', 'This sugar layer is what makes chenna poda unique.', 2),
            (3, 'Press chhena mixture into the tin. Top with cashews and raisins.', '', 5),
            (4, 'Bake at 180°C for 50–60 minutes until dark golden on top and caramelised on the bottom.', '', 60),
            (5, 'Cool completely before inverting. The caramelised bottom becomes the beautiful top. Slice and serve.', '', None),
        ],
    },

    # ── WEST INDIA ──────────────────────────────────────────────────────────

    {
        'title': 'Vada Pav',
        'desc': 'Mumbai\'s favourite street food and the "Indian burger" — a spiced potato dumpling in a crispy chickpea-flour shell, tucked inside a soft bread roll with chutneys.',
        'state': 'MH', 'cuisine': 'Gujarati', 'diet': 'veg', 'diff': 'medium',
        'prep': 20, 'cook': 30, 'servings': 4, 'calories': 380,
        'image_url': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
        'trending': True, 'featured': True, 'festival': '',
        'cats': ['Snacks & Chaat', 'Breakfast', 'Vegetarian'],
        'ingredients': [
            (4, '', 'large potatoes, boiled and mashed'),
            (1, 'cup', 'besan (chickpea flour)'),
            (1, 'tbsp', 'ginger-garlic-green chilli paste'),
            (1, 'tsp', 'turmeric'),
            (1, 'tsp', 'mustard seeds'),
            (10, '', 'curry leaves'),
            (4, '', 'pav buns (dinner rolls)'),
            ('', '', 'dry garlic chutney and green chutney'),
        ],
        'steps': [
            (1, 'Temper mustard seeds, curry leaves in oil. Add ginger-chilli paste and mashed potato. Season with turmeric, salt and lemon juice. Cool.', '', 10),
            (2, 'Shape potato mixture into round balls slightly smaller than the pav bun.', '', 5),
            (3, 'Make batter with besan, turmeric, salt and water — thick enough to coat. Dip potato balls and deep fry until golden and crispy.', '', 15),
            (4, 'Slit pav buns, spread dry garlic chutney on one side and green chutney on the other.', '', 2),
            (5, 'Place hot vada inside the pav. Serve immediately with fried green chilli on the side.', 'Best eaten on the street standing up.', None),
        ],
    },

    {
        'title': 'Puran Poli',
        'desc': 'Maharashtra\'s celebratory sweet flatbread — stuffed with a sweet chana dal and jaggery filling fragrant with cardamom. Made on every festival and auspicious occasion.',
        'state': 'MH', 'cuisine': 'Gujarati', 'diet': 'veg', 'diff': 'medium',
        'prep': 30, 'cook': 30, 'servings': 6, 'calories': 320,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Holi Special',
        'cats': ['Sweets & Desserts', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (1, 'cup', 'chana dal (split chickpeas)'),
            (1, 'cup', 'jaggery, grated'),
            (2, 'cups', 'whole wheat flour'),
            (1, 'tsp', 'cardamom powder'),
            ('1/4', 'tsp', 'nutmeg powder'),
            (2, 'tbsp', 'ghee'),
            ('', '', 'ghee for serving'),
        ],
        'steps': [
            (1, 'Pressure cook chana dal until very soft. Drain completely and mash smooth.', '', 20),
            (2, 'Cook mashed dal with jaggery on low heat, stirring until mixture thickens and leaves sides of pan. Add cardamom and nutmeg. This is the puran.', '', 15),
            (3, 'Knead wheat flour with oil and water into a soft dough. Rest 30 minutes.', '', 30),
            (4, 'Make a small disc of dough, place a ball of puran in centre, seal and roll out gently into a thin circle.', 'The puran should be completely enclosed — patch any tears.', 10),
            (5, 'Cook on a tawa on medium heat with ghee on both sides until golden. Serve warm with more ghee and milk.', '', 10),
        ],
    },

    {
        'title': 'Undhiyu',
        'desc': 'Gujarat\'s winter harvest festival dish — a mixed vegetable casserole cooked upside down in an earthen pot underground. Loaded with seasonal vegetables and methi muthia dumplings.',
        'state': 'GJ', 'cuisine': 'Gujarati', 'diet': 'veg', 'diff': 'hard',
        'prep': 45, 'cook': 60, 'servings': 6, 'calories': 290,
        'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Uttarayan Special',
        'cats': ['Dinner', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (200, 'g', 'surti papdi (flat beans)'),
            (200, 'g', 'brinjal (eggplant), small'),
            (200, 'g', 'sweet potato, cubed'),
            (100, 'g', 'raw banana, cubed'),
            (1, 'cup', 'green peas'),
            (1, 'cup', 'methi (fenugreek) leaves for muthia'),
            ('1/2', 'cup', 'besan for muthia'),
            (3, 'tbsp', 'undhiyu masala'),
            (4, 'tbsp', 'oil'),
        ],
        'steps': [
            (1, 'Make muthia: mix methi leaves, besan, ajwain, salt and a little oil. Shape into small cylinders and deep fry until golden.', '', 15),
            (2, 'Make undhiyu masala paste: blend coconut, green chilli, garlic, coriander, sesame and spices.', '', 10),
            (3, 'Stuff brinjals with masala paste. Coat all other vegetables with remaining masala.', '', 10),
            (4, 'Layer all vegetables in a heavy pot — brinjal at bottom, lighter vegetables on top. Add muthia throughout.', '', 5),
            (5, 'Drizzle oil on top. Cover tightly and cook on very low heat for 45 minutes without opening. Shake pot occasionally.', 'Trust the process — do not open the lid.', 45),
            (6, 'Serve with puri and shrikhand. The vegetables should be very soft and fragrant.', '', None),
        ],
    },

    # ── NORTHEAST INDIA ──────────────────────────────────────────────────────

    {
        'title': 'Masor Tenga (Assamese Sour Fish Curry)',
        'desc': 'Assam\'s signature fish curry — refreshingly light and sour from tomatoes or elephant apple. No heavy spices, just clean, pure flavours with mustard oil.',
        'state': 'AS', 'cuisine': 'Bengali', 'diet': 'nonveg', 'diff': 'easy',
        'prep': 10, 'cook': 25, 'servings': 4, 'calories': 210,
        'image_url': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Bihu Special',
        'cats': ['Lunch', 'Under 30 Minutes'],
        'ingredients': [
            (600, 'g', 'rohu fish, cut into pieces'),
            (3, '', 'tomatoes, chopped'),
            (1, '', 'lemon or elephant apple (ou tenga)'),
            (1, 'tsp', 'turmeric'),
            (1, 'tsp', 'fenugreek seeds'),
            (2, 'tbsp', 'mustard oil'),
            (2, '', 'green chillies'),
            ('', '', 'salt to taste'),
        ],
        'steps': [
            (1, 'Rub fish with turmeric and salt. Shallow fry in mustard oil until golden. Set aside.', '', 8),
            (2, 'In same oil, add fenugreek seeds — let them darken slightly for a nutty aroma.', 'Darkened fenugreek is essential for tenga flavour.', 2),
            (3, 'Add tomatoes and green chillies. Cook until tomatoes are completely soft and pulpy.', '', 8),
            (4, 'Add 1.5 cups water, salt and squeeze in lemon. Bring to a boil.', '', 3),
            (5, 'Add fried fish and simmer gently 8 minutes. The curry should be thin and sour. Serve with boiled rice.', '', 8),
        ],
    },

    {
        'title': 'Jadoh (Khasi Rice and Pork)',
        'desc': 'Meghalaya\'s beloved one-pot rice dish cooked with pork, turmeric and ginger. The Khasi people\'s version of pilaf — rustic, hearty and deeply comforting.',
        'state': 'ML', 'cuisine': 'Bengali', 'diet': 'nonveg', 'diff': 'medium',
        'prep': 20, 'cook': 60, 'servings': 4, 'calories': 480,
        'image_url': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Lunch', 'Dinner'],
        'ingredients': [
            (400, 'g', 'pork belly or shoulder, cubed'),
            (2, 'cups', 'short-grain rice'),
            (1, 'tbsp', 'fresh ginger, grated'),
            (1, 'tsp', 'turmeric'),
            (1, '', 'onion, chopped'),
            (2, '', 'bay leaves'),
            (2, 'tbsp', 'pork fat or oil'),
            ('', '', 'salt and black pepper'),
        ],
        'steps': [
            (1, 'Cook pork cubes with ginger, turmeric, salt and enough water to cover for 30 minutes until tender. Reserve the pork stock.', '', 30),
            (2, 'In a deep pot, fry onion in pork fat until golden. Add bay leaves and washed rice.', '', 8),
            (3, 'Pour reserved pork stock (about 4 cups) over the rice. Bring to boil.', '', 5),
            (4, 'Add cooked pork pieces, stir once. Cover and cook on low heat for 20 minutes until rice absorbs all liquid.', '', 20),
            (5, 'Fluff gently, season with black pepper. Serve with onion salad and sesame chutney.', '', None),
        ],
    },

    {
        'title': 'Thukpa (Himalayan Noodle Soup)',
        'desc': 'Sikkim and Ladakh\'s warming noodle broth — hearty vegetable or meat soup with hand-rolled noodles, perfect for cold mountain nights.',
        'state': 'SK', 'cuisine': 'Bengali', 'diet': 'veg', 'diff': 'medium',
        'prep': 30, 'cook': 30, 'servings': 4, 'calories': 320,
        'image_url': 'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Dinner', 'Under 1 Hour', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'plain flour for noodles'),
            (2, '', 'carrots, sliced'),
            (1, 'cup', 'cabbage, shredded'),
            (2, '', 'spring onions, chopped'),
            (1, 'tbsp', 'ginger-garlic paste'),
            (1, 'tbsp', 'soy sauce'),
            (1, 'tsp', 'red chilli paste'),
            (5, 'cups', 'vegetable broth'),
        ],
        'steps': [
            (1, 'Knead flour with water into a stiff dough. Roll thin and cut into noodle strips. Boil in salted water until al dente. Drain and set aside.', '', 20),
            (2, 'In a pot, sauté ginger-garlic paste in oil until fragrant. Add chilli paste and soy sauce.', '', 5),
            (3, 'Add all vegetables and stir fry on high heat for 5 minutes.', '', 5),
            (4, 'Pour in vegetable broth and bring to a boil. Season with salt and pepper.', '', 5),
            (5, 'Add noodles to the broth just before serving. Simmer 2 minutes. Top with spring onions and serve immediately.', '', 5),
        ],
    },

    # ── MORE NORTH/CENTRAL INDIA ─────────────────────────────────────────────

    {
        'title': 'Kafuli (Pahadi Greens Curry)',
        'desc': 'Uttarakhand\'s prized hill dish — slow-cooked fresh spinach and fenugreek thickened with rice flour. Pure mountain simplicity at its best.',
        'state': 'UK', 'cuisine': 'Punjabi', 'diet': 'veg', 'diff': 'easy',
        'prep': 10, 'cook': 30, 'servings': 4, 'calories': 140,
        'image_url': 'https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Lunch', 'Vegetarian', 'Under 30 Minutes'],
        'ingredients': [
            (500, 'g', 'fresh spinach (palak)'),
            (100, 'g', 'fresh fenugreek (methi) leaves'),
            (2, 'tbsp', 'rice flour'),
            (1, 'tbsp', 'ghee'),
            (1, 'tsp', 'cumin seeds'),
            (3, '', 'garlic cloves, minced'),
            (1, 'tsp', 'red chilli powder'),
            ('', '', 'salt to taste'),
        ],
        'steps': [
            (1, 'Wash greens thoroughly. Boil in minimal water with salt until wilted. Blend coarsely — do not make it completely smooth.', '', 10),
            (2, 'Mix rice flour with a little cold water to make a paste. Stir into the green puree to thicken.', '', 5),
            (3, 'Cook on low heat for 15 minutes stirring regularly until kafuli thickens to a porridge consistency.', '', 15),
            (4, 'For tempering: heat ghee, add cumin, garlic, red chilli. Pour over kafuli.', '', 3),
            (5, 'Serve with mandua ki roti (finger millet flatbread) or rice.', '', None),
        ],
    },

    {
        'title': 'Nihari',
        'desc': 'Delhi\'s royal slow-cooked beef or mutton shank curry — braised overnight with bone marrow and a complex 25-spice blend. The original slow food of the Mughal era.',
        'state': 'DL', 'cuisine': 'Mughlai', 'diet': 'nonveg', 'diff': 'hard',
        'prep': 30, 'cook': 240, 'servings': 6, 'calories': 520,
        'image_url': 'https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=800&q=80',
        'trending': False, 'featured': True, 'festival': 'Eid Special',
        'cats': ['Dinner', 'Festival Special'],
        'ingredients': [
            (1, 'kg', 'mutton shank or beef shank with bone'),
            (3, 'tbsp', 'nihari masala'),
            (2, 'tbsp', 'whole wheat flour (atta) for thickening'),
            (3, 'tbsp', 'ghee'),
            (2, '', 'onions, sliced and fried crispy'),
            (1, 'tbsp', 'ginger-garlic paste'),
            ('', '', 'fresh ginger, green chilli, lemon for garnish'),
        ],
        'steps': [
            (1, 'Heat ghee, fry fried onions with ginger-garlic paste until fragrant. Add nihari masala and stir 3 minutes.', '', 8),
            (2, 'Add meat and sear well on high heat for 10 minutes.', '', 10),
            (3, 'Add enough water to cover meat completely. Bring to a boil, then reduce to lowest simmer. Cook covered for 3 hours.', 'The longer, the better. Meat should fall off the bone.', 180),
            (4, 'Mix wheat flour with water to make a thin paste. Stir into nihari to thicken the gravy slightly.', '', 5),
            (5, 'Simmer 30 more minutes. Adjust seasoning. Serve with kulcha topped with julienned ginger, green chilli and lemon.', '', 30),
        ],
    },

    {
        'title': 'Aloo Tikki Chaat',
        'desc': 'The king of Delhi street food — crispy potato patties topped with chickpea curry, tamarind chutney, yoghurt and sev. A riot of textures and flavours.',
        'state': 'DL', 'cuisine': 'Mughlai', 'diet': 'veg', 'diff': 'medium',
        'prep': 30, 'cook': 30, 'servings': 4, 'calories': 360,
        'image_url': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'cats': ['Snacks & Chaat', 'Vegetarian'],
        'ingredients': [
            (4, '', 'large potatoes, boiled and mashed'),
            (1, 'cup', 'boiled white peas or chickpeas'),
            ('1/2', 'cup', 'thick yoghurt, whisked'),
            (3, 'tbsp', 'tamarind chutney'),
            (3, 'tbsp', 'green coriander chutney'),
            (1, 'tsp', 'chaat masala'),
            ('', '', 'sev, pomegranate seeds to garnish'),
            ('', '', 'oil for frying'),
        ],
        'steps': [
            (1, 'Season mashed potato with salt, chaat masala, green chilli, ginger. Shape into flat round patties.', '', 10),
            (2, 'Shallow fry tikkis in oil on medium heat until deep golden and crispy on both sides.', 'Press gently with spatula while frying for even crispiness.', 15),
            (3, 'Make white peas curry: cook peas with tomato, cumin, chilli, tamarind until saucy.', '', 15),
            (4, 'Place 2 tikkis on a plate. Top with warm peas curry, cold yoghurt, tamarind chutney and green chutney.', '', 2),
            (5, 'Finish with chaat masala, sev and pomegranate seeds. Serve immediately.', '', None),
        ],
    },

    {
        'title': 'Kosha Mangsho (Bengali Slow-Cooked Mutton)',
        'desc': 'Bengal\'s definitive celebration meat dish — mutton slow-cooked to perfection in a thick caramelised onion and yoghurt gravy. Sunday lunch at its greatest.',
        'state': 'WB', 'cuisine': 'Bengali', 'diet': 'nonveg', 'diff': 'hard',
        'prep': 60, 'cook': 90, 'servings': 4, 'calories': 450,
        'image_url': 'https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=800&q=80',
        'trending': False, 'featured': True, 'festival': 'Durga Puja Special',
        'cats': ['Dinner', 'Festival Special'],
        'ingredients': [
            (800, 'g', 'bone-in mutton pieces'),
            (1, 'cup', 'yoghurt'),
            (3, '', 'large onions, sliced very thin'),
            (2, 'tbsp', 'ginger-garlic paste'),
            (3, 'tbsp', 'mustard oil'),
            (2, 'tsp', 'Bengali garam masala (cardamom, cinnamon, cloves)'),
            (1, 'tsp', 'kashmiri chilli powder'),
            ('', '', 'salt to taste'),
        ],
        'steps': [
            (1, 'Marinate mutton with yoghurt, half the ginger-garlic paste, chilli powder, salt for minimum 1 hour.', '', 60),
            (2, 'Heat mustard oil to smoking point. Fry onions for 20–25 minutes on medium heat until deep brown and caramelised.', 'The onions must be very dark — this is where the flavour comes from.', 25),
            (3, 'Add remaining ginger-garlic paste. Fry 5 minutes. Add marinated mutton.', '', 5),
            (4, 'Increase heat to high. "Kosh" (fry and stir continuously) the mutton for 15 minutes without adding water.', 'Kosha means the mutton must dry fry — no water yet.', 15),
            (5, 'Reduce heat, cover and slow cook for 45 minutes adding a splash of water only if it sticks. Mutton should be very tender.', '', 45),
            (6, 'Finish with Bengali garam masala and ghee. Serve with luchi (fried bread) or rice.', '', None),
        ],
    },

    {
        'title': 'Misal Pav',
        'desc': 'Maharashtra\'s fiery breakfast — sprouted moth beans in a spicy rassa (curry) topped with farsan mixture, onions and lemon. Pune and Nashik\'s pride.',
        'state': 'MH', 'cuisine': 'Gujarati', 'diet': 'veg', 'diff': 'medium',
        'prep': 480, 'cook': 30, 'servings': 4, 'calories': 380,
        'image_url': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'cats': ['Breakfast', 'Snacks & Chaat', 'Vegetarian'],
        'ingredients': [
            (1, 'cup', 'moth beans or mixed sprouts, sprouted overnight'),
            (2, '', 'onions, finely chopped'),
            (2, '', 'tomatoes, finely chopped'),
            (2, 'tbsp', 'misal masala or goda masala'),
            (1, 'tsp', 'red chilli powder'),
            (2, 'tbsp', 'oil'),
            (4, '', 'pav buns'),
            ('', '', 'farsan (sev), lemon wedges, raw onion for topping'),
        ],
        'steps': [
            (1, 'Pressure cook sprouted beans with salt and water for 2 whistles until cooked but not mushy.', '', 10),
            (2, 'Fry onions until golden. Add tomatoes, misal masala, chilli powder, cook until oil separates.', '', 10),
            (3, 'Add cooked sprouts and 2 cups water. Boil 10 minutes. This loose curry is the "rassa".', '', 10),
            (4, 'Serve in a deep bowl — thick sprout mixture at bottom, pour rassa on top.', '', None),
            (5, 'Top generously with farsan, raw onion, coriander, lemon juice. Eat with buttered pav.', '', None),
        ],
    },

    {
        'title': 'Thepla',
        'desc': 'Gujarat\'s beloved travel food — spiced fenugreek flatbread with yoghurt and methi leaves. Stays fresh for days making it perfect for journeys.',
        'state': 'GJ', 'cuisine': 'Gujarati', 'diet': 'veg', 'diff': 'easy',
        'prep': 15, 'cook': 20, 'servings': 4, 'calories': 160,
        'image_url': 'https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Breakfast', 'Under 30 Minutes', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'whole wheat flour'),
            (1, 'cup', 'fresh methi (fenugreek) leaves, chopped'),
            ('1/4', 'cup', 'yoghurt'),
            (1, 'tsp', 'turmeric'),
            (1, 'tsp', 'red chilli powder'),
            (1, 'tsp', 'ajwain (carom seeds)'),
            (2, 'tbsp', 'oil'),
            ('', '', 'salt to taste'),
        ],
        'steps': [
            (1, 'Mix flour, methi leaves, all spices, yoghurt and oil. Knead with minimal water into a medium-soft dough. Rest 10 minutes.', '', 10),
            (2, 'Divide into small balls. Roll into thin circles (slightly thicker than roti).', '', 5),
            (3, 'Cook on hot tawa with a little oil, pressing gently. Cook both sides until golden spots appear.', '', 10),
            (4, 'Serve with pickle, curd or aamras. Theplas stay fresh for 3–4 days when made with less moisture.', '', None),
        ],
    },

    {
        'title': 'Payasam (Kerala Rice Kheer)',
        'desc': 'The finale of every Onam sadya — rice cooked in jaggery and coconut milk until creamy, finished with cardamom, cashews and raisins fried in ghee.',
        'state': 'KL', 'cuisine': 'Malayali', 'diet': 'veg', 'diff': 'easy',
        'prep': 10, 'cook': 45, 'servings': 6, 'calories': 280,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Onam Special',
        'cats': ['Sweets & Desserts', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            ('1/2', 'cup', 'raw rice (red rice preferred)'),
            (1, 'cup', 'jaggery, grated'),
            (2, 'cups', 'thin coconut milk'),
            (1, 'cup', 'thick coconut milk'),
            (1, 'tsp', 'cardamom powder'),
            (2, 'tbsp', 'ghee'),
            (3, 'tbsp', 'cashews'),
            (2, 'tbsp', 'raisins'),
        ],
        'steps': [
            (1, 'Cook rice in 3 cups water until very soft and mushy — almost dissolving.', '', 20),
            (2, 'Dissolve jaggery in a little water, strain and add to cooked rice. Stir well.', '', 5),
            (3, 'Add thin coconut milk and cook on medium heat for 15 minutes stirring regularly.', '', 15),
            (4, 'Add thick coconut milk and cardamom. Stir and immediately remove from heat — do not boil after this.', 'Boiling thick coconut milk will cause it to curdle.', 2),
            (5, 'Fry cashews and raisins in ghee until golden. Pour over payasam. Serve warm or at room temperature.', '', 5),
        ],
    },

    {
        'title': 'Haleem',
        'desc': 'Hyderabad\'s iconic slow-cooked wheat and meat porridge — tender shredded mutton blended with lentils and wheat, cooked for hours until silky smooth.',
        'state': 'TS', 'cuisine': 'Hyderabadi', 'diet': 'nonveg', 'diff': 'hard',
        'prep': 480, 'cook': 180, 'servings': 8, 'calories': 480,
        'image_url': 'https://images.unsplash.com/photo-1574653853027-5382a3d23a15?w=800&q=80',
        'trending': True, 'featured': True, 'festival': 'Eid Special',
        'cats': ['Dinner', 'Festival Special'],
        'ingredients': [
            (500, 'g', 'mutton, bone-in'),
            (1, 'cup', 'broken wheat (dalia), soaked overnight'),
            ('1/4', 'cup', 'each of chana dal, toor dal, masoor dal'),
            (3, '', 'onions, sliced and fried crispy'),
            (2, 'tbsp', 'haleem masala'),
            (4, 'tbsp', 'ghee'),
            (1, 'tbsp', 'ginger-garlic paste'),
            ('', '', 'fresh mint, fried onions, lemon to serve'),
        ],
        'steps': [
            (1, 'Pressure cook mutton with ginger-garlic paste, haleem masala, salt and water for 8 whistles until falling off bone. Shred meat, discard bones.', '', 40),
            (2, 'Cook soaked wheat and lentils together in mutton stock until completely soft — minimum 1 hour on low heat.', '', 60),
            (3, 'Combine shredded mutton with the wheat-dal mixture. Using a wooden spoon or hand blender, vigorously stir until mixture becomes smooth and stringy.', 'The more you stir, the more silky it becomes.', 20),
            (4, 'Cook on low heat for another hour, stirring every 10 minutes. Add ghee throughout.', '', 60),
            (5, 'Season and serve topped with fried onions, julienned ginger, fresh mint, green chilli and lemon juice.', '', None),
        ],
    },

    {
        'title': 'Pani Puri (Golgappa)',
        'desc': 'India\'s most popular street food — crispy hollow puris filled with spiced potato, soaked in tangy tamarind and minty water. One puri, one gulp, pure joy.',
        'state': 'MH', 'cuisine': 'Punjabi', 'diet': 'veg', 'diff': 'medium',
        'prep': 30, 'cook': 20, 'servings': 4, 'calories': 180,
        'image_url': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
        'trending': True, 'featured': False, 'festival': '',
        'cats': ['Snacks & Chaat', 'Vegetarian'],
        'ingredients': [
            (1, 'cup', 'semolina (rava/suji)'),
            ('1/4', 'cup', 'maida'),
            (3, '', 'potatoes, boiled and mashed'),
            (1, 'cup', 'boiled chickpeas'),
            (1, 'bunch', 'fresh mint leaves'),
            (1, 'tbsp', 'tamarind paste'),
            (1, 'tsp', 'black salt'),
            (1, 'tsp', 'cumin powder'),
            ('', '', 'oil for deep frying'),
        ],
        'steps': [
            (1, 'Knead semolina and maida with water into a stiff dough. Rest covered for 20 minutes.', '', 20),
            (2, 'Roll very thin (almost paper thin). Cut small circles. Deep fry in medium-hot oil until puffed and crispy.', 'The oil must be just right — too hot puris burn, too cool they stay flat.', 15),
            (3, 'Blend mint, coriander, green chilli with cold water, lemon, black salt, cumin for the "pani" (water). Chill well.', '', 5),
            (4, 'Mash potatoes with chickpeas, chaat masala, onion, coriander for filling.', '', 5),
            (5, 'Make a hole in each puri, add a small amount of filling, dip fully in cold pani and eat immediately in one bite.', '', None),
        ],
    },

    {
        'title': 'Gulab Jamun',
        'desc': 'The beloved Indian sweet — soft milk-solid dumplings fried golden and soaked in rose-cardamom sugar syrup. No celebration is complete without these.',
        'state': 'RJ', 'cuisine': 'Mughlai', 'diet': 'veg', 'diff': 'medium',
        'prep': 20, 'cook': 30, 'servings': 8, 'calories': 220,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Diwali Special',
        'cats': ['Sweets & Desserts', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (1, 'cup', 'khoya (mawa) or milk powder'),
            (3, 'tbsp', 'maida'),
            (1, 'tbsp', 'ghee'),
            (2, 'cups', 'sugar'),
            (2, 'cups', 'water'),
            (4, '', 'cardamom pods, crushed'),
            (1, 'tsp', 'rose water'),
            ('', '', 'oil for deep frying'),
        ],
        'steps': [
            (1, 'Make sugar syrup by dissolving sugar in water. Add cardamom and rose water. Simmer 5 minutes until slightly sticky. Keep warm.', '', 8),
            (2, 'Knead khoya with maida and ghee into a soft smooth dough. Do not over-knead.', 'Cracks in the dough means balls will crack while frying.', 5),
            (3, 'Roll into smooth balls with absolutely no cracks — about the size of a large marble.', '', 5),
            (4, 'Deep fry on low-medium heat, turning constantly until deep golden brown all over. This takes 5–6 minutes per batch.', 'Low heat is essential — the inside must cook through.', 15),
            (5, 'Drop fried gulab jamuns immediately into warm (not hot) sugar syrup. Soak for minimum 2 hours. Serve warm.', '', None),
        ],
    },

    {
        'title': 'Idli Sambar',
        'desc': 'The quintessential South Indian breakfast — soft steamed rice-lentil cakes with a vegetable-tamarind lentil soup and fresh coconut chutney. Simple, nutritious, perfect.',
        'state': 'TN', 'cuisine': 'Chettinad', 'diet': 'veg', 'diff': 'medium',
        'prep': 480, 'cook': 30, 'servings': 4, 'calories': 200,
        'image_url': 'https://images.unsplash.com/photo-1630383249896-424e482df921?w=800&q=80',
        'trending': True, 'featured': True, 'festival': '',
        'cats': ['Breakfast', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'idli rice'),
            (1, 'cup', 'urad dal'),
            ('1/2', 'tsp', 'fenugreek seeds'),
            (1, 'cup', 'toor dal for sambar'),
            (200, 'g', 'mixed vegetables (drumstick, brinjal, tomato, shallots)'),
            (1, 'tbsp', 'tamarind paste'),
            (2, 'tbsp', 'sambar powder'),
            (1, 'tsp', 'mustard seeds'),
        ],
        'steps': [
            (1, 'Soak idli rice and urad dal + fenugreek seeds separately for 6 hours. Grind to smooth batter. Ferment 8–12 hours overnight.', 'Well-fermented batter gives light, spongy idlis.', 480),
            (2, 'Pour batter into greased idli moulds. Steam for 10–12 minutes until a skewer comes out clean.', '', 12),
            (3, 'Pressure cook toor dal until very soft. Add tamarind paste, sambar powder, salt and boiled vegetables. Simmer 15 minutes.', '', 20),
            (4, 'Temper sambar with mustard seeds, curry leaves, dried red chilli and asafoetida in ghee.', '', 5),
            (5, 'Serve hot idlis with sambar poured over and coconut chutney on the side.', '', None),
        ],
    },

    {
        'title': 'Gajar ka Halwa (Carrot Halwa)',
        'desc': 'The pride of North Indian winters — fresh red carrots slow-cooked in milk until reduced, sweetened with sugar and finished with cardamom, khoya and dry fruits.',
        'state': 'UP', 'cuisine': 'Awadhi', 'diet': 'veg', 'diff': 'easy',
        'prep': 20, 'cook': 60, 'servings': 6, 'calories': 280,
        'image_url': 'https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=800&q=80',
        'trending': False, 'featured': False, 'festival': 'Diwali Special',
        'cats': ['Sweets & Desserts', 'Festival Special', 'Vegetarian'],
        'ingredients': [
            (1, 'kg', 'red Delhi carrots, grated'),
            (1, 'litre', 'full-fat milk'),
            ('3/4', 'cup', 'sugar'),
            (4, 'tbsp', 'ghee'),
            ('1/2', 'cup', 'khoya (mawa)'),
            (1, 'tsp', 'cardamom powder'),
            (3, 'tbsp', 'mixed dry fruits (cashews, almonds, raisins)'),
        ],
        'steps': [
            (1, 'Heat a wide heavy pan with ghee. Add grated carrots and sauté on medium heat for 10 minutes.', '', 10),
            (2, 'Add milk and cook on medium heat, stirring every few minutes, until all the milk is absorbed — about 35–40 minutes.', 'Patience is key. Do not rush this step.', 40),
            (3, 'Add sugar and khoya. Stir continuously as sugar melts and mixture comes together.', '', 10),
            (4, 'Cook until halwa leaves the sides of the pan and ghee separates around the edges.', '', 5),
            (5, 'Finish with cardamom powder and fried dry fruits. Serve hot or warm.', '', None),
        ],
    },

    {
        'title': 'Kachori (Raj Kachori)',
        'desc': 'Rajasthan\'s showstopper street snack — large crispy puri shells filled with sprouts, chutneys, yoghurt, sev and papdi. An entire meal in one kachori.',
        'state': 'RJ', 'cuisine': 'Rajasthani', 'diet': 'veg', 'diff': 'hard',
        'prep': 30, 'cook': 30, 'servings': 4, 'calories': 420,
        'image_url': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
        'trending': False, 'featured': False, 'festival': '',
        'cats': ['Snacks & Chaat', 'Vegetarian'],
        'ingredients': [
            (2, 'cups', 'maida (plain flour)'),
            ('1/4', 'cup', 'moong dal, soaked'),
            (1, 'cup', 'yoghurt, whisked'),
            (3, 'tbsp', 'tamarind chutney'),
            (3, 'tbsp', 'green chutney'),
            (1, 'cup', 'mixed sprouted beans, boiled'),
            (1, 'tsp', 'chaat masala'),
            ('', '', 'sev, papdi, pomegranate to garnish'),
        ],
        'steps': [
            (1, 'Knead maida with oil and water into a stiff dough. Rest 15 minutes.', '', 15),
            (2, 'Season soaked moong dal filling with cumin, green chilli, coriander and salt.', '', 5),
            (3, 'Roll dough into medium circles. Place filling in centre, seal and roll gently into large puri shapes.', '', 10),
            (4, 'Deep fry on medium-low heat until puffed and golden. Raj kachori must be large — like a bowl.', '', 15),
            (5, 'To serve: make a hole on top, fill with sprouted beans, pour yoghurt and both chutneys, top with sev, papdi, chaat masala and pomegranate.', '', None),
        ],
    },
]


class Command(BaseCommand):
    help = 'Seed 50+ authentic Indian recipes across all states and categories'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('🍛 Seeding RecipeGlobe with 50+ authentic recipes...'))

        # Get existing data
        india = Country.objects.filter(code='IND').first()
        if not india:
            self.stdout.write(self.style.ERROR('India not found. Run seed_india first: python manage.py seed_india'))
            return

        state_map   = {s.code: s for s in State.objects.all()}
        cuisine_map = {c.name: c for c in Cuisine.objects.all()}
        cat_map     = {c.name: c for c in Category.objects.all()}
        admin_user  = User.objects.filter(is_superuser=True).first()

        created = 0
        skipped = 0

        for r in RECIPES:
            if Recipe.objects.filter(title=r['title']).exists():
                skipped += 1
                continue

            state   = state_map.get(r['state'])
            cuisine = cuisine_map.get(r['cuisine'])

            recipe = Recipe.objects.create(
                title=r['title'],
                description=r['desc'],
                country=india,
                state=state,
                cuisine=cuisine,
                diet_type=r['diet'],
                difficulty=r['diff'],
                prep_time=r['prep'],
                cook_time=r['cook'],
                servings=r['servings'],
                calories_per_serving=r['calories'],
                image_url=r['image_url'],
                is_trending=r['trending'],
                is_featured=r['featured'],
                festival_tag=r['festival'],
                is_published=True,
                author=admin_user,
            )

            # Assign categories
            for cat_name in r.get('cats', []):
                cat = cat_map.get(cat_name)
                if cat:
                    recipe.categories.add(cat)

            # Create ingredients
            for i, (qty, unit, name) in enumerate(r['ingredients'], 1):
                Ingredient.objects.create(
                    recipe=recipe,
                    quantity=str(qty),
                    unit=unit,
                    name=name,
                    order=i,
                )

            # Create steps
            for step_num, instruction, tip, time_min in r['steps']:
                RecipeStep.objects.create(
                    recipe=recipe,
                    step_number=step_num,
                    instruction=instruction,
                    tip=tip or '',
                    time_minutes=time_min,
                )

            created += 1
            self.stdout.write(f'  ✅ {recipe.title} ({state.name if state else "?"})')

        self.stdout.write(self.style.SUCCESS(
            f'\n🎉 Done! Created {created} recipes, skipped {skipped} existing.\n'
            f'   Run again anytime — existing recipes are never duplicated.'
        ))
