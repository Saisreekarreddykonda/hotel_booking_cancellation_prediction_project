import pandas as pd
import joblib
import numpy as np

#loading the model
model=joblib.load('models/xgboost_cancellation_model.pkl')

#function to load new input
def load_input_data():

    return pd.DataFrame([{

        # Numerical features
        'lead_time':50,
        'arrival_date_year':2025,
        'arrival_date_week_number':28,
        'arrival_date_day_of_month':15,
        'stays_in_weekend_nights':2,
        'stays_in_week_nights':3,
        'adults':2,
        'children':0,
        'babies':0,
        'is_repeated_guest':0,
        'previous_cancellations':0,
        'previous_bookings_not_canceled':0,
        'booking_changes':0,
        'days_in_waiting_list':0,
        'adr':100.5,
        'required_car_parking_spaces':1,
        'total_of_special_requests':1,
        'is_company_missing':1,
        'total_stay':5,
        'total_guests':2,
        'is_family':1,
        'is_weekend_stay':1,
        'is_repeated_customer':0,
        'room_mismatch':0,

        # One-hot encoded categorical features
        'hotel_Resort Hotel':True,

        # Arrival month
        'arrival_date_month_August':False,
        'arrival_date_month_December':False,
        'arrival_date_month_February':False,
        'arrival_date_month_January':False,
        'arrival_date_month_July':True,
        'arrival_date_month_June':False,
        'arrival_date_month_March':False,
        'arrival_date_month_May':False,
        'arrival_date_month_November':False,
        'arrival_date_month_October':False,
        'arrival_date_month_September':False,

        # Meal type
        'meal_FB':False,
        'meal_HB':False,
        'meal_SC':True,
        'meal_Undefined':False,

        # Market segment
        'market_segment_Complementary':False,
        'market_segment_Corporate':False,
        'market_segment_Direct':False,
        'market_segment_Groups':False,
        'market_segment_Offline TA/TO':False,
        'market_segment_Online TA':True,
        'market_segment_Undefined':False,

        # Distribution channel
        'distribution_channel_Direct':False,
        'distribution_channel_GDS':False,
        'distribution_channel_TA/TO':True,
        'distribution_channel_Undefined':False,

        # Deposit type
        'deposit_type_Non Refund':False,
        'deposit_type_Refundable':False,

        # Customer type
        'customer_type_Group':False,
        'customer_type_Transient':True,
        'customer_type_Transient-Party':False,

        # Season
        'season_Rainy':False,
        'season_Spring':False,
        'season_Summer':True,
        'season_Winter':False,

        # Country grouping
        'country_grouped_BRA':False,
        'country_grouped_DEU':False,
        'country_grouped_ESP':False,
        'country_grouped_FRA':False,
        'country_grouped_GBR':True,
        'country_grouped_IRL':False,
        'country_grouped_ITA':False,
        'country_grouped_NLD':False,
        'country_grouped_Other':False,
        'country_grouped_PRT':False
    }])

# Function to predict cancellation
def predict_cancellation(data):
    prediction=model.predict(data)
    probability=model.predict_proba(data)[0][1] #probablity of class "1" (canceled)
    return int(prediction[0]),round(probability,3)

if __name__=="__main__":
    input_data=load_input_data()
    prediction,prob=predict_cancellation(input_data)

    print("Prediction:","Canceled" if prediction==1 else "Not Canceled")
    print("Probability of cancellation:",prob)