


from bs4 import BeautifulSoup
import requests ,json
import  lxml ,re
# fetch data from the youtube search page

r=requests.get(url="https://www.youtube.com/results?search_query=sql+and+python")
print(r.raise_for_status())

# if r.status_code==200:
#     # Make a soup
#     soup=BeautifulSoup(r.text,"lxml")
#     print(soup.prettify())
#     with open(r"Sacraping-Website\\01-text.html","w",encoding="utf-8") as f:
#         f.write(soup.prettify())
        
# else:
#     print("error")



with open(r"Sacraping-Website\\01-text.html","r",encoding="utf-8") as f:
    soup=BeautifulSoup(f,"html.parser")


# print(soup.prettify())




# print(soup.a)

print(soup.find("svg"))
script_tag=soup.find_all("script")
# print(script_tag[6])

# Extract the JSON data from the relevant script tag
for script in script_tag:
    if script.string and "var ytInitialData =" in script.string:
        # use regrax to capture the json  data within the curly braces
        json_str=re.search(r"var ytInitialData = ({.*?});", script.string, re.DOTALL).group(1)
        
        # # Correctly extract the JSON string
        # json_data = script.string.split("var ytInitialData = ")[1].rstrip(' ;')
        
        # Convert the JSON string to a Python dictionary
        data = json.loads(json_str)
        
        # Save the JSON data to a file (optional)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        break

# Load the JSON data from the file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.loads(f)

# Gather the video data from the JSON file
video_data = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
# Print out the video data
for video in video_data:
    if 'videoRenderer' in video:
        video_info = video['videoRenderer']
        title = video_info['title']['runs'][0]['text']
        video_url = f"https://www.youtube.com/watch?v={video_info['videoId']}"
        channel_name = video_info['ownerText']['runs'][0]['text']
        view_count = video_info.get('viewCountText', {}).get('simpleText', 'N/A')
        upload_date = video_info.get('publishedTimeText', {}).get('simpleText', 'N/A')

        print(f"Title: {title}")
        print(f"URL: {video_url}")
        print(f"Channel: {channel_name}")
        print(f"Views: {view_count}")
        print(f"Uploaded: {upload_date}")
        print('-' * 40)