from datetime import datetime

API_KEY = "2052420657:AAHLqVzRPvBca74olM_7QjL6H8GQbljq3XY"

userGreetings = ["hello", "hey", "yo", "sup"]
userQuestions = ["who are you", "who are you ?", "who are you ??"]

facts = [
    "π Akshaya Patra feeds 1,800,907 children every day across India",
    "π Akshaya Patra covers 16,800+ schools across 12 states & 2 Union Territories and has 52 state-of-the-art kitchens under its belt",
    "π The Akshaya Patra Foundation operates in 55 kitchens across 13 States & 1 Union Territory of India",
    "π On February 19th, 2019, Akshaya Patra's Mid-day Meal Scheme became the worldβs first NGO-run school meal programme to serve 3 billion cumulative meals.",
    "π All food is prepared hygienically in kitchens that have ISO 22000:2005 certification.",
    "π As a part of MID DAY MEAL programme any individual or organisation can sponsor upto 5000 government school children at the cost of approximately Rs. 1100/- per child per year. ",
    "π The foundation aims to make every part of production including the kitchens that feed millions of people as green and sustainable as possible.",
    "π Akshaya Patra has decentralized kitchens set up in Baran, Rajasthan and Nayagarh, Odisha reaching out to 161 schools and 319 schools respectively",
    "π Akshaya Patraβs role as a food and nutrition provider for nearly two decades has enabled it to garner significant knowledge and experience. The Foundation is deeply rooted in its service to the children of India. ",
    "π Currently, there are 55 highly automated kitchens across 14 states serving 1.8 million children dailyβ under the Akshaya Patra foundation. ",
    "π The Akshaya Patra Foundation won the prestigious 14th Mother Teresa Award in the Best NGO category. ",
    "π Anganwadi Centres (AWCs) established under the umbrella of the Integrated Child Development Services (ICDS) are central to tackling the issue of intergenerational malnutrition. One of the primary goals of setting up AWCs is to improve the nutritional intake.",
    "π Akshaya Patra Foundation is the Only NGO in ICAI Hall of Fame for earning 7-time Gold Shield Award for Excellence in Financial Reportingβ. ",
    "π The prestigious Gandhi Peace Prize for the year 2016 was conferred upon Akshaya Patra for its contribution towards socio-economic development. ",
    "π The Honβble President of India, Shri Ramnath Kovind conferred the National Award for Child Welfare 2017 on Akshaya Patra. ",
    "π The Honβble President of India, Shri Ramnath Kovind conferred the National Award for Child Welfare 2017 on Akshaya Patra. ",
    "π Akshaya Patra has been awarded the βKalam Innovation in Governanceβ Award. ",
    "π Currently, Akshaya Patra  implements the mid-day meal programme in 19,039 schools of the country, with plans to increase that number to hundreds more.",
    "π Akshaya Patra was honoured with the ICAI Gold Shield Award for βExcellence in Financial Reporting' for the year 2017-18 in the Not-for-Profit Sector for the 7th time in a row, to become the only NGO in the 70-year history of ICAI that has won this distinction.",
    "π Akshaya Patra has won the CSR TIMES Award 2018 under the category βEradicating Extreme Hunger, Poverty and Malnutrition",
    "π Akshaya Patra has won the CSR TIMES Award 2018 under the category βEradicating Extreme Hunger, Poverty and Malnutritionβ",
    "π Akshaya Patra upholds absolute transparency in all its activities. For this purpose, we comply with the International Financial Reporting Standards (IFRS). We also comply with the Indian Accounting Standards issued by the Institute of Chartered Accountants of India (ICAI) . At the end of each financial year, an Annual Report with financial audits and statements is published and made available to the stakeholders.",
    "π In the aftermath of the Nepal earthquake in April 2015, a relief kitchen was set up in collaboration with Tata Trusts and Sipradian Sahayata Sanstha (SSS) in Bhaktapur, Nepal. Akshaya Patra served approximately 1.4 million meals over 88 days.",
    "π Akshaya Patra has already served over 18.72Cr Covid-19 Relief meals",
    "π Looking out of a window, one day in Mayapur, a village near Calcutta, His Divine Grace A. C. Bhaktivedanta Swami Prabhupada saw a group of children fighting with stray dogs over scraps of food. From this simple, yet heart-breaking incident was born a determination that no child within a radius of ten miles from our centre should go hungry.",
    "π Looking out of a window, one day in Mayapur, a village near Calcutta, His Divine Grace A. C. Bhaktivedanta Swami Prabhupada saw a group of children fighting with stray dogs over scraps of food. From this simple, yet heart-breaking incident was born a determination that no child within a radius of ten miles from our centre should go hungry.",
    "π Akshaya Patra is focused on eliminating classroom hunger and attracting more children (enrolment) to schools and ensure to keep them in school (reduce dropout rate) by feeding a filling, nutritious mid-day meal, every school day. This is in partnership with the Government of India and all the various State Governments. ",
    "π The Akshaya Patra Foundation is a not-for-profit organisation headquartered in Bengaluru, India. ",
    "π  Akshaya Patra kitchens are technology-driven, which ensures the entire cooking process is untouched by human hand. These centralized, automated kitchens can cook close to 6,000 kg of rice, 4.5-5 tonne of vegetables and 6,000 litres of sambar, in under six hours. ",
    "π  Akshaya Patra has a strategic approach towards achieving the UN Sustainable Development Goals (SDGs) by directly contributing to SDG 2 β Zero Hunger, SDG 4 β Quality Education, and SDG 5 β Gender Equality through the Mid-Day Meal (MDM) Programme.",
]


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in userGreetings:
        return "Hello! Hope you are doing well!"
    elif user_message in userQuestions:
        return "I am a bot"
    else:
        return "I don't know what you mean"
