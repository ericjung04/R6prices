import requests
import json

# The GraphQL endpoint
url = "https://public-ubiservices.ubi.com/v1/profiles/me/uplay/graphql"

# The cleaned-up GraphQL query
query = """
query GetItemPriceHistory($spaceId: String!, $itemId: String!, $paymentItemId: String!) {
  game(spaceId: $spaceId) {
    id
    marketableItem(itemId: $itemId) {
      id
      priceHistory(paymentItemId: $paymentItemId) {
        id
        date
        lowestPrice
        averagePrice
        highestPrice
        itemsCount
        __typename
      }
      __typename
    }
    __typename
  }
}
"""

# The variables extracted from the Network tab
variables = {
    "spaceId": "0d2ae42d-4c27-4cb7-af6c-2099062302bb",
    "itemId": "f619eb19-de6e-4dcd-96eb-08b45f80fe64",
    "paymentItemId": "9ef71262-515b-46e8-b9a8-b6b6ad456c67"
}

# Headers with the Authorization token
headers = {
    "Content-Type": "application/json",
    "Authorization": "ubi_v1 t=ewogICJ2ZXIiOiAiMSIsCiAgImFpZCI6ICI5OWY1OGIzMi0xZmU2LTRlZmMtOTQyZi0xNDNjZTc3OWZhYzIiLAogICJlbnYiOiAiUHJvZCIsCiAgInNpZCI6ICJmOGM3NTE2Ni03YTYyLTQ4YTUtOGVlNC03YjhjY2ZhYTM3ZTEiLAogICJ0eXAiOiAiSldFIiwKICAiZW5jIjogIkExMjhDQkMiLAogICJpdiI6ICJGZUZ2cGtpOU1OeEFQUjBEazRtQTdRIiwKICAiaW50IjogIkhTMjU2IiwKICAia2lkIjogIjJiOWM4ODZmLTM1Y2EtNDc4OS05MTgzLTk2NmY5MTVhZjcyOCIKfQ.JCLJ9X1F1U2pKiFweJGVrDQKprauYKsXsRLhf6iEVIl7StqLI-79_Twkl2Aago7-mHPrbmeEzwy5LPQiIF9imFk2JafoQpleSzAtqzcGKtHgQtbaoN33tB-sTJVEjkULTtITY0kEARPBBagq3_vK4LJ7z1KLPMt_RmaXC8H9Nn3gyv-h0qEn9ivn2praxIQr1N34tjCAU1Vgjo7nORaxhMUQouDCQmvXTV4-Ow0M7D2FUK-OhbKfanX1q5anCAxxwFlj0Z5V7yMggMQDkxiyLfwA6jlJQRIpVFa9JCwFsXTgAiq_XEFrtXrdW1xYJZEwy6q-YSLgOzerzaoy1Mv7OrRY6t16OD3bBMKrxSAADiwr_fngufWY5UCdH-ofIgLh7BP4IXx1xTlSoTydaQNCNN3NqiOZut6zoJXgEssGA67VoUJw33LSngPkSvIJsk4q9SkOdkHnEW0UYaA8YjKNV4CPJG3lnMFv7XencUmN1E7_rPO_XF9aTdOZigu3mGdceW701knEmXRSZrnIi76chIi29R19fhzNSX8C-YpKMdwfQ1ZDdeL_dz2gyevkwgMvi5Cxpr-eSgGW1An2dtgnQ1pnJU9-PsPWkBohMdE5CZlJM8uaXTJ0pzJy9jwlkyA-OauVz4CS6BFDoIE1OnV57X4vFtWtONQw4lX2eDQcy2ZqTv1uzOSH-InqZzh8tOx4IL24cOX7X1xIeiMc1Sq0Qvld2cCeAt_ryU_92jfhVEZvDp3tKiWMTmqfFIT_cXJeAFHvfn5i4mvRabgeyWgGgBXnbkCwD-6W661VBiVabiApcqN4Ozu_UTObMXguPCm3AW8JNbgO0P4nS3302tljkQzlTrhPjSyc2RS85EOEiIm0SENjNd1UL1xKI1VQzus--F9hT7sC-h_rPISE5yLXvwu3VAr9CzxnwKBQJOPSyOJruaNZ375R7tWIGAPNWU8P33FSbYgd6i7XIMQluMlbSlXXq183j-pS3Kuu2G1sH6u7tyJ3KLdjzvxM07YVa_Q76FLjJkJrvvqG63Fi-fUGXh8DlyMGr7gF-0CNptSG0I53D-K7jrWUdt_Aesmjf_b77uPzSi1lDkBWeX1-X-FrQavytmdCgb-H_lVT76R72TFlBKChENKERLl6IEfj1CvLDRMNeNReoX4xt6WdfGjsYr__9a1TDwhlReROGavCAoGB1MEPRTOJmiac6yJLRV_-p8LLnvd8PnQ5P6Wvx89rIJ7S4c3O4lHmDhf8a7xKnAGaf9gI9ZJ2tcvSo-frPUrzsJJjDhWo5CSjorXXmIcwAAEr7rXniun29qjUwxKbKkqBpYZEdkGQf8jW-kwVl3hQAgIL8A0HpqApy9wnLto_anI4EtbEzs2R0emYWC9D_pqcJua_z6ht9xPV2Vv4JqRQTgIerLxY8pW9t46B3fqqOs5PWkunYeVmuOdNzyIFW62PODaM5KS9NI_2PgCzR7nNsddMqJxdGHXItWYETIj9psk8RCrqatc1RBurCqVujjan_W3Ke-jnPpMtHnG2uLL0_mfv4hu3Nrze7Qu4F-LtdQtAwdK__zgrfngbE8N_pni1yCyW7nzvRZKFqh2ql1mEB8gitor3AdVZN9w0_BgvLOULiivlVqO5eaycSD1wDeMyTUIL3FCW8Qe9wUUDetN0IzOApv2LAsBt2e-M7ITk3v1Tus62FeE6AwejSxQTNSp_PZLXVlagKTf-QsmBzU5meIgulevVGc2onvxBYPJ2cnXoUV5_c9YAkVvuxTUFqUqD7-TNpuMEtWISGljkpuGYxuoV1Oy_ZHT1DTWsjfcQ2ewwrr7WU6hAdcTR_ZNwpqC-8FQZ8o5Me8ym6xACDtlvvwHb-m86bR8T1-3t-p_odFbuEitdJS3kjZkMpO6jZ606zFXlDsxJSvBWvpvaWXXiBk9L4HtiTQohvNi1oIuEUBLo6Jn0-zL7Ds-xqRAdxW1BURiJOGC86s_lfZlvhUFAFUw_3UdCOkEQaGBvdqnn0ody74CVwL5fCkIkLYudKA3SNkgGcq7uVkS3Bpk8fR4YHT1X3gdGz38lc5MXn_iMFyr7UKprapiUwmSlDKWtii8LZlpZkyas-A_4YblFrQKN2jP8aHF3Usg-Tp_NNco7YglZE6MN5wiEWIogD2mxSlSMa9VRq0A1K69w_-z_eMa-rNqyVxWgr0WZR3xjubOxqne2DnViHu2UmTteGynNP9cVOt6Y91tV7N-ScWkVs3tWOGSl2MroNy-aXRRkTnrUkT4O--KeSMEtWkrNSzQjC0SCWKGD3-XMF89bP87anZz5fp8DmTxdnfWLfZiz0zTysOBSsjLf9Hg3tLgQLN4_WV5oJibLpjoqNcffiv1Ln-Qxww1KRrkYCjOz3IeTBtmrMEi3canqtEG4abWGWXkSg73E9pTP2GDKYmAEUZ0n-QHZYvwQ2UBDnK6S4BkNS0O7WvMKno7OW0AZHlLZXx9HF7NlH8fZtzeaZsuCrt7qwfZCuj7rHmVT-dJD8E69ai1M7xhY5yajUDhvW51l2IumWP0nLzYT_QB1siw4S0MoKCjwlb1Jh03gxYqNXSl-5Z9HtfeHuOhrZg4LUAIk2gjxbdDYD6Y4gvnO-rD6SjwKLIHjRCoxhLDk7FDuCwiZmQap6FAdjhj8naCVWdHVfFzj-o21Lq8H-8AN6EnQkSr57RWBLLYUjrG-zfQiGwtZXTg0Xl3p9QyX_kzZD7jt86LX_DV1bkB7d5TNcfCpUoZV2-_QZb4qBgEPgX-eDkb3Dr1SgPTt-wXqP3nPrrCPCj5iaE_eI52d8eOy3HnbsgLyw7Uqe1jqD6nWzMs2KqZCX9PdGRxr6OA2sD9GIFWGGqZoz4HZAT7AO9rwOSax-5wzWtLdKMPF12pStyLONLjriiGJxhK_Hg81S-1qBKmkNBpR8qAmE5Xmos25Tt4_bpXonAkH7YvSGM4xCZhk9y3OIuOqa0kyz4lI1ZOvj7pOsRKxp4oBknN7U0qC9cgD2kK26rsj.AQCh-NFzXbCZ74ZTuYiD0zmT0Xx2zSTepNC7Wh578pg"
}

# The request payload
payload = {
    "operationName": "GetItemPriceHistory",
    "query": query,
    "variables": variables
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the price history data
    price_history = data['data']['game']['marketableItem']['priceHistory']
    
    # Print the price history data
    for day in price_history:
        print(f"Date: {day['date']}, Lowest Price: {day['lowestPrice']}, Average Price: {day['averagePrice']}, Highest Price: {day['highestPrice']}, Items Count: {day['itemsCount']}")
else:
    print(f"Failed to fetch data: {response.status_code}")
