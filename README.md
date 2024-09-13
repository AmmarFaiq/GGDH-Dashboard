GGDH Dashboard Ver 1.6

Link :
https://ggdh-dashboard.onrender.com 

This is one of the ongoing dashboard projects for GGDH-ELAN from the Department of Public Health and Primary Care at LUMC / Health Campus the Hague. In the current version, there are a few notes that we need to be aware of :

1. Area coverage (will increase in the future):

- ELAN covered area :

 - Den Haag and other : s-Gravenhage, Leidschendam-Voorburg, Rijswijk, Wassenaar
 - Leiden and other : Alphen aan den Rijn, Hillegom, Kaag en Braassem, Katwijk, Leiden, Leiderdorp, Lisse, Nieuwkoop, Noordwijk, Oegstgeest, Teylingen, Voorschoten, Zoeterwoude
 - Delft and other: Delft, Midden-Delfland, Pijnacker-Nootdorp, Westland
 - Zoetermeer
 - Additional : Waddinxveen, Bodegraven-Reeuwijk

- Hadoks Area : 's-Gravenhage, Leidschendam-Voorburg, Rijswijk, Wassenaar
 
2. Working pages are :

- Neighbourhood: contains infographics of past variables per Neighbourhood.
- Supply and Demand: contains a clustering and projection of selected variables per Neighbourhood in Collaboration with Hadoks
- heartfailure: contains infographics of heart failure patients
- Language options are working only on Neighbourhood (main page)
  
3. Multiple pages still "work-in-progress" (Diabetes, Palliative care and Pedriatic care)
4. Utility pages still work in progress (About Us, Variables Explanation, Data Availability, Changelog)

-- Ammar, Lisette, Marcel

What we can do to improve :

1. Use parquet for faster and lighter data 

2. hack and slash: server separated for different functions, data processing in other server, and visualization on the other

3. Use more standard web tools besides dash so it is more flexible in web visualization (maybe jquery).

4. Name of rijswijk Wijk : https://www.rijswijk.nl/de-wijken-van-rijswijk (proabbly not changing the name since it is just combination of buurt name)




