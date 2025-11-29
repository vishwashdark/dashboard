from pymongo import MongoClient

# MongoDB connection details
MONGO_URI = "mongodb+srv://sans:sans@cluster0.7db5ls2.mongodb.net/?appName=Cluster0"
DB_NAME = "aegis_db"
COLLECTION_NAME = "instagram"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# User data to insert (with ai_generated flag)
data = [
  {
    "user_name": "ava_carter",
    "user_pass": "ava123",
    "user_followers": 4320,
    "user_gender": "female",
    "user_revenue": 1120.50,
    "user_profile": "style/images/Ava_Carter_profile.png",
    "user_post_1": {
      "image_path": "style/images/Ava_Carter_mountain.png",
      "caption": "Chasing horizons 🌄✨",
      "date": "2025-01-11",
      "time": "07:50",
      "ai_generated": True
    },
    "user_post_2": {
      "image_path": "style/images/Ava_Carter_Paris_cafe.png",
      "caption": "Croissants and dreams ☕🥐",
      "date": "2025-01-13",
      "time": "10:22",
      "ai_generated": True
    }
  },

  {
    "user_name": "leo_thompson",
    "user_pass": "leo123",
    "user_followers": 5980,
    "user_gender": "male",
    "user_revenue": 890.75,
    "user_profile": "style/images/Leo_Thomson_profile.png",
    "user_post_1": {
      "image_path": "style/images/Leo_Thomson_running.png",
      "caption": "Run your own race 🏃🔥",
      "date": "2025-01-09",
      "time": "06:45",
      "ai_generated": True
    },
    "user_post_2": {
      "image_path": "style/images/Leo_Thomson_protein_bowl(real).jpg",
      "caption": "Fueling gains one bowl at a time 💪🥗",
      "date": "2025-01-12",
      "time": "13:18",
      "ai_generated": False
    }
  },

  {
    "user_name": "maya_rivera",
    "user_pass": "maya123",
    "user_followers": 7120,
    "user_gender": "female",
    "user_revenue": 1560.20,
    "user_profile": "style/images/Maya_Rivera_profile.png",
    "user_post_1": {
      "image_path": "style/images/Maya_Rivera_art_gallery(real).jpg",
      "caption": "Finding inspiration between the strokes 🎨✨",
      "date": "2025-01-08",
      "time": "14:10",
      "ai_generated": False
    },
    "user_post_2": {
      "image_path": "style/images/Maya_Rivera_textile_exhibition(real).jpg",
      "caption": "Textile art brings stories to life 🧵🌟",
      "date": "2025-01-14",
      "time": "16:30",
      "ai_generated": False
    }
  }
]

# Insert into MongoDB
result = collection.insert_many(data)

print("Inserted document IDs:")
print(result.inserted_ids)
