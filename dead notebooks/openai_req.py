from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")

def text_request(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def image_request():
  response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What’s in this image?"},
                  {
                      "type": "image_url",
                      "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                  },
              ],
          }
      ],
      max_tokens=300,
  )
  print(response.choices[0].message.content)
  return response.choices[0].message.content

def multi_image_request():
  response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What are in these images? Is there any difference between them?",
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )
  print(response.choices[0])


import base64
import requests

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def data_image_request():

  # Path to your image
  image_path = "nutriscoreVecoscore.png"

  # Getting the base64 string
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  content = response.json()['choices'][0]['message']['content']
  print(content)
  return content


if __name__ == "__main__":
    # text_request("What is recursion in programming?")
    # image_request()
    data_image_request()
    # 'This image is a scatter plot graph comparing Nutriscore Score to Ecoscore Score by Food Group Category. 
    # The X-axis represents the Nutriscore Score ranging from approximately -15 to 35, while the Y-axis represents the Ecoscore Score from about -20 to 120.
    # \n\nDifferent colored dots represent various food groups: Beverages, Cereals and potatoes, Composite foods, Fat and sauces, 
    # Fish meat eggs, Fruits and vegetables, Milk and dairy products, Salty snacks, and Sugary snacks. Each food group is also associated with a colored trendline, 
    # indicating the relationship between the Nutriscore and the Ecoscore within that particular category.\n\nThe scatter plot is dense with data points, 
    # suggesting a considerable amount of variability within each food group regarding their nutritional and environmental impacts as measured by these scores.
    # The trendlines for each category show the general tendency or correlation between the two scores for each type of food.'