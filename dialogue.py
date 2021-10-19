from datetime import datetime

API_KEY = "2052420657:AAHLqVzRPvBca74olM_7QjL6H8GQbljq3XY"

userGreetings = ["hello", "hey", "yo", "sup"]
userQuestions = ["who are you", "who are you ?", "who are you ??"]

facts = [
    "📌 Akshaya Patra feeds 1,800,907 children every day across India",
    "📌 Akshaya Patra covers 16,800+ schools across 12 states & 2 Union Territories and has 52 state-of-the-art kitchens under its belt",
    "📌 The Akshaya Patra Foundation operates in 55 kitchens across 13 States & 1 Union Territory of India",
    "📌 On February 19th, 2019, Akshaya Patra's Mid-day Meal Scheme became the world’s first NGO-run school meal programme to serve 3 billion cumulative meals.",
    "📌 All food is prepared hygienically in kitchens that ISO 22000:2005 certified.",
    "📌 As a part of MID DAY MEAL programme any individual or organisation can sponsor upto 5000 government school children at the cost of approximately Rs. 1100/- per child per year. ",
    "📌 The foundation aims to make every part of production including the kitchens that feed millions of people as green and sustainable as possible.",
    "📌 Akshaya Patra has decentralized kitchens set up in Baran, Rajasthan and Nayagarh, Odisha reaching out to 161 schools and 319 schools respectively",
    "📌 Akshaya Patra’s role as a food and nutrition provider for nearly two decades has enabled it to garner significant knowledge and experience. The Foundation is deeply rooted in its service to the children of India. ",
    "📌 Currently, there are 55 highly automated kitchens across 14 states serving 1.8 million children daily​ under the Akshaya Patra foundation. ",
    "📌 The Akshaya Patra Foundation won the prestigious 14th Mother Teresa Award in the Best NGO category. ",
    "📌 Anganwadi Centres (AWCs) established under the umbrella of the Integrated Child Development Services (ICDS) are central to tackling the issue of intergenerational malnutrition. One of the primary goals of setting up AWCs is to improve the nutritional intake.",
    "📌 Akshaya Patra Foundation is the Only NGO in ICAI Hall of Fame for earning 7-time Gold Shield Award for Excellence in Financial Reporting​. ",
    "📌 The prestigious Gandhi Peace Prize for the year 2016 was conferred upon Akshaya Patra for its contribution towards socio-economic development. ",
    "📌 The Hon’ble President of India, Shri Ramnath Kovind conferred the National Award for Child Welfare 2017 on Akshaya Patra. ",
    "📌 The Hon’ble President of India, Shri Ramnath Kovind conferred the National Award for Child Welfare 2017 on Akshaya Patra. ",
    "📌 Akshaya Patra has been awarded the ‘Kalam Innovation in Governance’ Award. ",
    "📌 Currently, Akshaya Patra  implements the mid-day meal programme in 19,039 schools of the country, with plans to increase that number to hundreds more.",
    "📌 Akshaya Patra was honoured with the ICAI Gold Shield Award for ‘Excellence in Financial Reporting' for the year 2017-18 in the Not-for-Profit Sector for the 7th time in a row, to become the only NGO in the 70-year history of ICAI that has won this distinction.",
    "📌 Akshaya Patra has won the CSR TIMES Award 2018 under the category ‘Eradicating Extreme Hunger, Poverty and Malnutrition",
    "📌 Akshaya Patra has won the CSR TIMES Award 2018 under the category ‘Eradicating Extreme Hunger, Poverty and Malnutrition’",
    "📌 Akshaya Patra upholds absolute transparency in all its activities. For this purpose, we comply with the International Financial Reporting Standards (IFRS). We also comply with the Indian Accounting Standards issued by the Institute of Chartered Accountants of India (ICAI) . At the end of each financial year, an Annual Report with financial audits and statements is published and made available to the stakeholders.",
    "📌 In the aftermath of the Nepal earthquake in April 2015, a relief kitchen was set up in collaboration with Tata Trusts and Sipradian Sahayata Sanstha (SSS) in Bhaktapur, Nepal. Akshaya Patra served approximately 1.4 million meals over 88 days.",
    "📌 Akshaya Patra has already served over 18.72Cr Covid-19 Relief meals",
    "📌 Looking out of a window, one day in Mayapur, a village near Calcutta, His Divine Grace A. C. Bhaktivedanta Swami Prabhupada saw a group of children fighting with stray dogs over scraps of food. From this simple, yet heart-breaking incident was born a determination that no child within a radius of ten miles from our centre should go hungry.",
]


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in userGreetings:
        return "Hello! Hope you are doing well!"
    elif user_message in userQuestions:
        return "I am a bot"
    else:
        return "I don't know what you mean"
