from services.youtube import search_youtube

song = input("🎵 What do you want to play? ")

result = search_youtube(song)

print(result["message"])