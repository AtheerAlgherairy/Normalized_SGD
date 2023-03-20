
original_domains=['Banks_1', 'Buses_1', 'Buses_2', 'Calendar_1', 'Events_1', 'Events_2', 'Flights_1',
                  'Flights_2', 'Homes_1', 'Hotels_1', 'Hotels_2', 'Hotels_3', 'Media_1', 'Movies_1', 
                  'Music_1', 'Music_2', 'RentalCars_1', 'RentalCars_2', 'Restaurants_1', 'RideSharing_1',
                  'RideSharing_2', 'Services_1', 'Services_2', 'Services_3', 'Travel_1', 'Weather_1', 'Alarm_1',
                  'Banks_2', 'Flights_3', 'Hotels_4', 'Media_2', 'Movies_2', 'Restaurants_2', 'Services_4',
                  'Buses_3', 'Events_3', 'Flights_4', 'Homes_2', 'Media_3', 'Messaging_1', 'Movies_3', 'Music_3',
                  'Payment_1', 'RentalCars_3', 'Trains_1']
domain_mapping = {
            'Hotel': ['Hotels_1', 'Hotels_2', 'Hotels_3', 'Hotels_4'],
            'Train': ['Trains_1'],
            'Attraction': ['Travel_1'],
            'Restaurant': ['Restaurants_1', 'Restaurants_2'],
            'RideSharing': ['RideSharing_1', 'RideSharing_2'],
            'Bus': ['Buses_1', 'Buses_2', 'Buses_3'],
            'Flight': ['Flights_1', 'Flights_2', 'Flights_3', 'Flights_4'],
            'Music': ['Music_1', 'Music_2', 'Music_3'],
            'Movie': ['Media_1', 'Media_2', 'Media_3','Movies_2', 'Movies_3'],
            'Cinema': ['Movies_1'],    
            'Dentist': [ 'Services_2'],
            'Doctor': ['Services_3'],
            'HairStylist': ['Services_1'],
            'Therapist': ['Services_4'],
            'Bank': ['Banks_1', 'Banks_2'],
            'Payment' : ['Payment_1'],
            'Event': ['Events_1', 'Events_2', 'Events_3'],
            'Rentalcar': ['RentalCars_1', 'RentalCars_2', 'RentalCars_3'],
            'Home': ['Homes_1', 'Homes_2'],
            'Calendar': ['Calendar_1'],
            'Weather': ['Weather_1'],
            'Alarm': ['Alarm_1'],
            'Messaging': ['Messaging_1']
        }



slot_mapping = {
            'Hotels_1': {
                'destination': 'city',
                'number_of_days': 'stay',
                'phone_number':'phone',
                'price_per_night':'price',
                'street_address':'address'
            },
            'Hotels_2': {
                'phone_number': 'phone' ,
                'rating': 'star_rating', 
                'total_price': 'price' ,
                'where_to': 'city'     
            },
            'Hotels_3': {
                'average_rating': 'star_rating',
                'location': 'city',
                'phone_number': 'phone',
                'street_address': 'address'
            },
            'Hotels_4': {
                'location':'city',
                'phone_number': 'phone',
                'place_name': 'hotel_name',
                'price_per_night': 'price',
                'street_address': 'address',
                'stay_length': 'stay'
            },
            'Trains_1': {
                'from': 'from_city',
                'journey_start_time': 'leave_at',
                'number_of_adults': 'number_of_persons',
                'to' : 'to_city'
            },
            'Travel_1':  {
                'location':'city' ,
                'phone_number':'phone' ,       
            },
            'Restaurants_1': {
                'phone_number': 'phone',
                'street_address':'address',
                'party_size': 'number_of_persons'
        
            },
            'Restaurants_2': {
                'category':  'cuisine',
                'phone_number': 'phone',
                'number_of_seats':'number_of_persons',
                 'location': 'city',
                  'rating': 'star_rating'
            },
    
    
            'RideSharing_1': {
                'number_of_riders': 'number_of_persons',
                'destination': 'destination_address',
        
            },
              'RideSharing_2': {
                'number_of_seats': 'number_of_persons',
                'destination': 'destination_address'
            },
        
            'Buses_1': {
                'from_location':  'from_city',
                'to_location':    'to_city',            
                'leaving_time':    'leave_at',
                'leaving_date':   'date',
                'travelers':       'number_of_persons',
                'fare' : 'price',
              
            },
    
            'Buses_2': {
                'destination': 'to_city',
                'destination_station_name' : 'to_station',
                'origin':          'from_city',
                'origin_station_name': 'from_station',
                'departure_time':   'leave_at',
                'group_size':       'number_of_persons',
                'departure_date':   'date',
            },
    
            'Buses_3': {

                'departure_time':    'leave_at',
                'departure_date':   'date',
                'num_passengers':  'number_of_persons'
            },
    
            'Flights_1': {
                'destination_city' : 'to_city',
                'origin_city': 'from_city',
                'passengers': 'number_of_persons'
            },
    
            'Flights_2': {
                'destination' : 'to_city',
                'origin': 'from_city',
                'passengers': 'number_of_persons',
                'fare':'price'
            },
    
            'Flights_3': {
                'destination_airport_name' :'destination_airport',
                'destination_city' : 'to_city',
                'origin_airport_name': 'origin_airport',
                'origin_city': 'from_city',
                'passengers': 'number_of_persons',
                'flight_class' : 'seating_class'
             },

            'Flights_4': {
                'number_of_tickets': 'number_of_persons',

            },
            'Music_3': {
                'track':'song_name',
                'device':'playback_device',
            },
            'Movies_1': {

                'location': 'city',
                'street_address': 'address',
                'number_of_tickets' : 'number_of_persons'
            },
            'Movies_2': {

                'aggregate_rating':'rating',
                'starring' : 'cast',
                'title': 'movie_name',
            },
            'Movies_3': {
      
                'directed_by': 'director',
                'percent_rating':'rating',
                'movie_title': 'movie_name',
            },
            'Media_1': {
        
                'directed_by': 'director',
                'subtitles':'has_subtitle',
                'title': 'movie_name',
            },
            'Media_2': {
                'actors' : 'cast'
            },
            'Media_3': {
                'title': 'movie_name',
                'starring' : 'cast',
            },
        'Services_1': {
                 'average_rating': 'rating',
                 'phone_number':'phone',
                 'street_address': 'address',
                 'appointment_date':'date',
                 'appointment_time':'time',
             },
    
         'Services_2': {
                 'phone_number':'phone',
                 'appointment_date':'date',
                 'appointment_time':'time',
         },
        'Services_3': {
                 'average_rating': 'rating',
                 'phone_number':'phone',
                 'street_address': 'address',
                 'appointment_date':'date',
                 'appointment_time':'time',
          },
         'Services_4': {         
                 'phone_number':'phone',
                 'appointment_date':'date',
                 'appointment_time':'time'
         },    
           'Banks_1': {
               'recipient_account_name': 'recipient',
           },
            'Banks_2': {
               'account_balance':'balance',
               'transfer_amount':'amount',
               'recipient_name': 'recipient'
           },
    
            'Payment_1': {
                'receiver':'recipient'
            },
    
            'Events_1': {
                'address_of_location':'address',
                'category':'event_category',
                'subcategory':'event_subcategory',
                'city_of_event': 'city',
                'event_location':'venue',
                'number_of_seats': 'number_of_persons'
            },
    
            'Events_2': {
                'venue_address':'address',
                'number_of_tickets':'number_of_persons',
                'category':'event_subcategory',
                'event_type':'event_category',  
            },

            'Events_3': {

                'event_type':'event_category',
                'number_of_tickets':'number_of_persons',
                'price_per_ticket':'price_per_ticket',
                'venue_address':'address',
            },
    
          'RentalCars_1': {
                'pickup_city':'city',
                'type':'car_type'
            },
            'RentalCars_2': {
                'pickup_city':'city'
            },
            'RentalCars_3': {
                'start_date':  'pickup_date',
                'end_date':    'dropoff_date'
            },
            'Homes_1': {
                'area':'city',
                'phone_number':'phone'
            },
            'Homes_2': {
                'area':'city',
                'phone_number':'phone'
            }
    
        }