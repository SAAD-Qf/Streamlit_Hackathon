
# doctor_agent.py
from agents import Agent, OpenAIChatCompletionsModel, function_tool ,set_tracing_disabled ,ModelSettings
from openai import AsyncOpenAI
import os
from whatsapp import send_whatsapp_message
from pydantic import BaseModel
from dotenv import load_dotenv

# ---------------- Setup Agent Model ---------------- #
set_tracing_disabled(disabled=True)
load_dotenv()



API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


# ---------------- User Data ---------------- #
user_pool =[
     {
    "id": '0',
    "name": 'Dr. Sarah Johnson',
    "specialty": 'General Medicine',
    "rating": 4.8,
    "availableTime": 'Available Now',
    "fee":'$50',
    "location": '2.5 km away',
   " image": 'https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg'
  },
  {
     "id": '1',
     "name": 'Dr Urusa Baloch',
    "specialty": 'Dermatoligst',
    "rating": 4.8,
    "availableTime": '24/7',
    "fee": '$50',
    "location": '2.5 km away',
    "image": 'https://th.bing.com/th?id=OIF.QgO20%2bxDzuVNnY6iR2ahpQ&rs=1&pid=ImgDetMain&o=7&rm=3'
  },
  {
    "id": '2',
    "name": 'Dr. Michael Chen',
    "specialty": 'Internal Medicine',
    "rating": 4.9,
    "availableTime": 'Next: 2:30 PM',
    "fee": '$65',
    "location": '1.8 km away',
    "image": 'https://images.pexels.com/photos/6205509/pexels-photo-6205509.jpeg'
  },
   {
        "id": "3",
        "name": "Dr. Emily Rodriguez",
        "specialty": "Family Medicine",
        "rating": 4.7,
        "availableTime": "Next: 4:00 PM",
        "fee": "$45",
        "location": "3.2 km away",
        "image": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg"
    },
    {
        "id": "4",
        "name": "Dr. David Kumar",
        "specialty": "Cardiology",
        "rating": 4.9,
        "availableTime": "Tomorrow 9:00 AM",
        "fee": "$80",
        "location": "4.1 km away",
        "image": "https://images.pexels.com/photos/6749773/pexels-photo-6749773.jpeg"
    },
    {
        "id": "5",
        "name": "Dr. Ayesha Malik",
        "specialty": "Dermatology",
        "rating": 4.6,
        "availableTime": "Today 6:00 PM",
        "fee": "$55",
        "location": "2.0 km away",
        "image": "https://images.pexels.com/photos/5327580/pexels-photo-5327580.jpeg"
    },
    {
        "id": "6",
        "name": "Dr. John Williams",
        "specialty": "Orthopedics",
        "rating": 4.8,
        "availableTime": "Tomorrow 11:30 AM",
        "fee": "$70",
        "location": "5.3 km away",
        "image": "https://images.pexels.com/photos/6303557/pexels-photo-6303557.jpeg"
    },
    {
        "id": "7",
        "name": "Dr. Priya Sharma",
        "specialty": "Gynecology",
        "rating": 4.7,
        "availableTime": "Available Now",
        "fee": "$60",
        "location": "3.7 km away",
        "image": "https://images.pexels.com/photos/1181685/pexels-photo-1181685.jpeg"
    },
    {
        "id": "8",
        "name": "Dr. Carlos Mendes",
        "specialty": "Neurology",
        "rating": 4.9,
        "availableTime": "Next: 5:00 PM",
        "fee": "$90",
        "location": "6.2 km away",
        "image": "https://images.pexels.com/photos/8460093/pexels-photo-8460093.jpeg"
    },
    {
        "id": "9",
        "name": "Dr. Fatima Noor",
        "specialty": "Pediatrics",
        "rating": 4.8,
        "availableTime": "Tomorrow 10:00 AM",
        "fee": "$50",
        "location": "1.9 km away",
        "image": "https://images.pexels.com/photos/5327899/pexels-photo-5327899.jpeg"
    },
    {
        "id": "10",
        "name": "Dr. Robert King",
        "specialty": "Oncology",
        "rating": 4.7,
        "availableTime": "Today 7:30 PM",
        "fee": "$120",
        "location": "7.1 km away",
        "image": "https://images.pexels.com/photos/7088527/pexels-photo-7088527.jpeg"
    },
    {
        "id": "11",
        "name": "Dr. Amna Javed",
        "specialty": "ENT Specialist",
        "rating": 4.6,
        "availableTime": "Next: 1:30 PM",
        "fee": "$40",
        "location": "3.4 km away",
        "image": "https://images.pexels.com/photos/3714743/pexels-photo-3714743.jpeg"
    },
    {
        "id": "12",
        "name": "Dr. Mark Allen",
        "specialty": "Psychiatry",
        "rating": 4.8,
        "availableTime": "Tomorrow 3:00 PM",
        "fee": "$85",
        "location": "4.9 km away",
        "image": "https://images.pexels.com/photos/5327581/pexels-photo-5327581.jpeg"
    },
    {
        "id": "13",
        "name": "Dr. Sana Qureshi",
        "specialty": "Endocrinology",
        "rating": 4.7,
        "availableTime": "Today 8:00 PM",
        "fee": "$75",
        "location": "2.7 km away",
        "image": "https://images.pexels.com/photos/8460100/pexels-photo-8460100.jpeg"
    },
    {
        "id": "14",
        "name": "Dr. James Lee",
        "specialty": "Urology",
        "rating": 4.8,
        "availableTime": "Available Now",
        "fee": "$95",
        "location": "5.8 km away",
        "image": "https://images.pexels.com/photos/6303554/pexels-photo-6303554.jpeg"
    },
    {
        "id": "15",
        "name": "Dr. Maria Santos",
        "specialty": "Gastroenterology",
        "rating": 4.6,
        "availableTime": "Tomorrow 12:00 PM",
        "fee": "$85",
        "location": "4.2 km away",
        "image": "https://images.pexels.com/photos/8460044/pexels-photo-8460044.jpeg"
    },
    {
        "id": "16",
        "name": "Dr. Bilal Hussain",
        "specialty": "Pulmonology",
        "rating": 4.9,
        "availableTime": "Next: 6:30 PM",
        "fee": "$70",
        "location": "6.0 km away",
        "image": "https://images.pexels.com/photos/5215026/pexels-photo-5215026.jpeg"
    },
    {
        "id": "17",
        "name": "Dr. Hannah Green",
        "specialty": "Ophthalmology",
        "rating": 4.8,
        "availableTime": "Today 5:15 PM",
        "fee": "$60",
        "location": "3.3 km away",
        "image": "https://images.pexels.com/photos/6234596/pexels-photo-6234596.jpeg"
    },
    {
        "id": "18",
        "name": "Dr. Zeeshan Rauf",
        "specialty": "Nephrology",
        "rating": 4.7,
        "availableTime": "Tomorrow 2:00 PM",
        "fee": "$110",
        "location": "7.5 km away",
        "image": "https://images.pexels.com/photos/6749771/pexels-photo-6749771.jpeg"
    },
    {
        "id": "19",
        "name": "Dr. Laura Bennett",
        "specialty": "Rheumatology",
        "rating": 4.6,
        "availableTime": "Next: 4:30 PM",
        "fee": "$95",
        "location": "6.7 km away",
        "image": "https://images.pexels.com/photos/7088530/pexels-photo-7088530.jpeg"
    },
    {
        "id": "20",
        "name": "Dr. Adnan Malik",
        "specialty": "Plastic Surgery",
        "rating": 4.9,
        "availableTime": "Today 9:00 PM",
        "fee": "$200",
        "location": "8.0 km away",
        "image": "https://images.pexels.com/photos/6749774/pexels-photo-6749774.jpeg"
    },
    {
        "id": "21",
        "name": "Dr. Kate Wilson",
        "specialty": "Allergy & Immunology",
        "rating": 4.7,
        "availableTime": "Tomorrow 11:00 AM",
        "fee": "$70",
        "location": "5.4 km away",
        "image": "https://images.pexels.com/photos/5327600/pexels-photo-5327600.jpeg"
    },
    {
        "id": "22",
        "name": "Dr. Usman Tariq",
        "specialty": "Infectious Disease",
        "rating": 4.8,
        "availableTime": "Next: 7:45 PM",
        "fee": "$90",
        "location": "6.1 km away",
        "image": "https://images.pexels.com/photos/5215029/pexels-photo-5215029.jpeg"
    },
    {
        "id": "23",
        "name": "Dr. Olivia Brown",
        "specialty": "Sports Medicine",
        "rating": 4.6,
        "availableTime": "Today 4:45 PM",
        "fee": "$65",
        "location": "3.9 km away",
        "image": "https://images.pexels.com/photos/6749775/pexels-photo-6749775.jpeg"
    },
    {
        "id": "24",
        "name": "Dr. Kamran Ahmed",
        "specialty": "Hematology",
        "rating": 4.8,
        "availableTime": "Tomorrow 1:00 PM",
        "fee": "$100",
        "location": "6.9 km away",
        "image": "https://images.pexels.com/photos/5327582/pexels-photo-5327582.jpeg"
    },
    {
        "id": "25",
        "name": "Dr. Sophia Martinez",
        "specialty": "Obstetrics",
        "rating": 4.7,
        "availableTime": "Today 8:30 PM",
        "fee": "$85",
        "location": "2.8 km away",
        "image": "https://images.pexels.com/photos/8460101/pexels-photo-8460101.jpeg"
    }
]

# ---------------- Tool ---------------- #
@function_tool
def get_user_data() -> list[dict]:
    return user_pool

# ---------------- Doctor Agent ---------------- #
dr_agent = Agent(
    name="Dr Agent",
    instructions="""
        You are an exceptional, highly knowledgeable, and empathetic doctor agent.
        Your role is to provide accurate and detailed information about doctors from the user database.
        Always respond clearly and politely, suggesting the best doctor based on the user's needs.
        You can provide doctor details such as name, specialty, rating, availability, consultation fee, location, and image.
        If asked, you can also send WhatsApp messages using send_whatsapp_message to notify or remind patients.
        Always double-check the information before providing it, and give concise, friendly, and professional responses.
        Try to personalize the interaction, using a human-like tone while remaining precise.
    """,
    model=model,
    tools=[get_user_data, send_whatsapp_message],
    model_settings=ModelSettings(temperature=0.9)
    
)
