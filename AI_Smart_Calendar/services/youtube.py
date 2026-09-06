import webbrowser
from urllib.parse import quote_plus


def search_youtube(query):
    """
    Search YouTube for whatever the user enters/says.
    """

    if query is None:
        return {
            "success": False,
            "message": "Please tell me what you want to play."
        }

    query = str(query).strip()

    if query == "":
        return {
            "success": False,
            "message": "Please tell me the song name."
        }

    # Create YouTube search URL
    search_url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )

    try:
        webbrowser.open(search_url)

        return {
            "success": True,
            "service": "youtube",
            "query": query,
            "url": search_url,
            "message": f"Searching YouTube for {query}"
        }

    except Exception as error:

        return {
            "success": False,
            "service": "youtube",
            "query": query,
            "message": str(error)
        }


def open_youtube():
    """
    Open YouTube homepage.
    """

    try:

        webbrowser.open("https://www.youtube.com")

        return {
            "success": True,
            "service": "youtube",
            "message": "Opening YouTube."
        }

    except Exception as error:

        return {
            "success": False,
            "service": "youtube",
            "message": str(error)
        }