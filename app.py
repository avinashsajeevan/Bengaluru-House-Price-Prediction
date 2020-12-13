import streamlit as st
import pandas as pd
import numpy as np
import pickle


# loading the trained model
pickle_in = open('banglore_home_prices_model.pickle', 'rb')
model = pickle.load(pickle_in)

# defining the function which will make the prediction using the data which the user inputs
def prediction(Location, total_sqft, bath, bhk):
    
    loc_index = np.where(x.columns==Location)[0][0]
    x = np.zeros(len(x.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
   return model.predict([x])[0]
    # Making predictions


# this is the main function in which we define our webpage
def run():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Bengaluru Home Price Prediction </h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    total_sqft =st.number_input('Area (Square Feet)' , min_value=1000, max_value=100000, value=1000)
    bath =st.number_input('Bathroom' , min_value=1, max_value=5, value=1)
    bhk =st.number_input('BHK' , min_value=1, max_value=5, value=1)
    Location = st.selectbox('Location', ("1st Block Jayanagar", "1st Phase JP Nagar", "2nd Phase Judicial Layout", "2nd Stage Nagarbhavi", "5th Block Hbr Layout", "5th Phase JP Nagar", "6th Phase JP Nagar", "7th Phase JP Nagar", "8th Phase JP Nagar", "9th Phase JP Nagar", "AECS Layout", "Abbigere", "Akshaya Nagar", "Ambalipura", "Ambedkar Nagar", "Amruthahalli", "Anandapura", "Ananth Nagar", "Anekal", "Anjanapura", "Ardendale", "Arekere", "Attibele", "BEML Layout", "BTM 2nd Stage", "BTM Layout", "Babusapalaya", "Badavala Nagar", "Balagere", "Banashankari", "Banashankari Stage II", "Banashankari Stage III", "Banashankari Stage V", "Banashankari Stage VI", "Banaswadi", "Banjara Layout", "Bannerghatta", "Bannerghatta Road", "Basavangudi", "Basaveshwara Nagar", "Battarahalli", "Begur", "Begur Road", "Bellandur", "Benson Town", "Bharathi Nagar", "Bhoganhalli", "Billekahalli", "Binny Pete", "Bisuvanahalli", "Bommanahalli", "Bommasandra", "Bommasandra Industrial Area", "Bommenahalli", "Brookefield", "Budigere", "CV Raman Nagar", "Chamrajpet", "Chandapura", "Channasandra", "Chikka Tirupathi", "Chikkabanavar", "Chikkalasandra", "Choodasandra", "Cooke Town", "Cox Town", "Cunningham Road", "Dasanapura", "Dasarahalli", "Devanahalli", "Devarachikkanahalli", "Dodda Nekkundi", "Doddaballapur", "Doddakallasandra", "Doddathoguru", "Domlur", "Dommasandra", "EPIP Zone", "Electronic City", "Electronic City Phase II", "Electronics City Phase 1", "Frazer Town", "GM Palaya", "Garudachar Palya", "Giri Nagar", "Gollarapalya Hosahalli", "Gottigere", "Green Glen Layout", "Gubbalala", "Gunjur", "HAL 2nd Stage", "HBR Layout", "HRBR Layout", "HSR Layout", "Haralur Road", "Harlur", "Hebbal", "Hebbal Kempapura", "Hegde Nagar", "Hennur", "Hennur Road", "Hoodi", "Horamavu Agara", "Horamavu Banaswadi", "Hormavu", "Hosa Road", "Hosakerehalli", "Hoskote", "Hosur Road", "Hulimavu", "ISRO Layout", "ITPL", "Iblur Village", "Indira Nagar", "JP Nagar", "Jakkur", "Jalahalli", "Jalahalli East", "Jigani", "Judicial Layout", "KR Puram", "Kadubeesanahalli", "Kadugodi", "Kaggadasapura", "Kaggalipura", "Kaikondrahalli", "Kalena Agrahara", "Kalyan nagar", "Kambipura", "Kammanahalli", "Kammasandra", "Kanakapura", "Kanakpura Road", "Kannamangala", "Karuna Nagar", "Kasavanhalli", "Kasturi Nagar", "Kathriguppe", "Kaval Byrasandra", "Kenchenahalli", "Kengeri", "Kengeri Satellite Town", "Kereguddadahalli", "Kodichikkanahalli", "Kodigehaali", "Kodigehalli", "Kodihalli", "Kogilu", "Konanakunte", "Koramangala", "Kothannur", "Kothanur", "Kudlu", "Kudlu Gate", "Kumaraswami Layout", "Kundalahalli", "LB Shastri Nagar", "Laggere", "Lakshminarayana Pura", "Lingadheeranahalli", "Magadi Road", "Mahadevpura", "Mahalakshmi Layout", "Mallasandra", "Malleshpalya", "Malleshwaram", "Marathahalli", "Margondanahalli", "Marsur", "Mico Layout", "Munnekollal", "Murugeshpalya", "Mysore Road", "NGR Layout", "NRI Layout", "Nagarbhavi", "Nagasandra", "Nagavara", "Nagavarapalya", "Narayanapura", "Neeladri Nagar", "Nehru Nagar", "OMBR Layout", "Old Airport Road", "Old Madras Road", "Padmanabhanagar", "Pai Layout", "Panathur", "Parappana Agrahara", "Pattandur Agrahara", "Poorna Pragna Layout", "Prithvi Layout", "R.T. Nagar", "Rachenahalli", "Raja Rajeshwari Nagar", "Rajaji Nagar", "Rajiv Nagar", "Ramagondanahalli", "Ramamurthy Nagar", "Rayasandra", "Sahakara Nagar", "Sanjay nagar", "Sarakki Nagar", "Sarjapur", "Sarjapur  Road", "Sarjapura - Attibele Road", "Sector 2 HSR Layout", "Sector 7 HSR Layout", "Seegehalli", "Shampura", "Shivaji Nagar", "Singasandra", "Somasundara Palya", "Sompura", "Sonnenahalli", "Subramanyapura", "Sultan Palaya", "TC Palaya", "Talaghattapura", "Thanisandra", "Thigalarapalya", "Thubarahalli", "Tindlu", "Tumkur Road", "Ulsoor", "Uttarahalli", "Varthur", "Varthur Road", "Vasanthapura", "Vidyaranyapura", "Vijayanagar", "Vishveshwarya Layout", "Vishwapriya Layout", "Vittasandra", "Whitefield", "Yelachenahalli", "Yelahanka", "Yelahanka New Town", "Yelenahalli", "Yeshwanthpur"))
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Location, total_sqft, bath, bhk)
        st.success('Estimated Price (in Lakhs) is {}'.format(result))

run()
