# SI 506: Iteration and Control Flow, Part II

import pprint

# fmt: off
# Includes faux test record (id=999999)
STATIONS = [
    ['id', 'station_name', 'facility_type', 'access_code', 'access_days_time', 'restricted_access', 'city', 'zip', 'street_address', 'intersection_directions', 'ev_network', 'ev_connector_types', 'ev_dc_fast_num', 'ev_level1_evse_num', 'ev_level2_evse_num', 'ev_other_evse', 'ev_pricing', 'date_last_confirmed'],
    ['41828', 'DTE Energy - Ann Arbor Ashley Mews Building', 'UTILITY', 'private ', 'Employee and official visitor use only, 24 hours daily with employee security badge', None, ' Ann Arbor ', '48104', '414 S Main St', 'Southeast corner of W Williams Street and S Ashley Street; in underground parking garage, entrance off of S Ashley Street; visitor parking spaces #1 and #2.', 'Non-Networked', 'J1772', None, None, '1', None, None, '2020-10-09'],
    ['42726', 'Ann Arbor Downtown Development Authority - Library Parking Structure', 'LIBRARY', ' public', '24 hours daily', 'False', 'Ann Arbor', '48104', '319 S Fifth Ave', 'Sift between Liberty and William', 'Non-Networked', 'J1772', None, None, '9', None, 'Variable parking fee', '2021-07-14'],
    ['44282', 'Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', ' PARKING GARAGE', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48104', '120 W Ann St', 'Ann and Ashley', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44283', 'Ann Arbor Downtown Development Authority - Catherine and Fourth Surface Lot', 'PARKING LOT ', ' public', '24 hours daily', 'False', 'Ann Arbor', '48104', '121 Catherine St', 'Catherine and Fourth', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44284', 'Ann Arbor Downtown Development Authority - Forrest Parking Structure', ' PARKING GARAGE', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48104', '650 Forrest St', 'Forrest and S University', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44285', 'Ann Arbor Downtown Development Authority - Maynard Parking Structure', ' PARKING GARAGE', ' public', '24 hours daily', 'False', 'Ann Arbor', '48104', '316 Maynard St', 'Maynard between Liberty and William', 'Non-Networked', 'J1772', None, None, '4', None, 'Variable parking fee', '2021-07-14'],
    ['44286', 'Ann Arbor Downtown Development Authority - William Street Parking Structure', ' PARKING GARAGE', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48104', '115 William St', 'William and Main', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44287', 'Ann Arbor Nissan', 'CAR_DEALER', ' public', 'Dealership business hours', 'False', 'Ann Arbor', '48103', '3975 Jackson Rd', None, 'Non-Networked', 'CHADEMO, J1772, J1772COMBO', '2', None, '1', None, 'Free', '2022-03-07'],
    ['44288', 'Ann Arbor Nissan', 'CAR_DEALER', 'private ', None, None, ' Ann Arbor ', '48103', '3975 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-03-07'],
    ['44773', 'IMRA America', 'OFFICE_BLDG', 'private', 'Employee and fleet use only', None, 'Ann Arbor', '48105', '1044 Woodridge Ave', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-06-14'],
    ['62417', 'U-M ANN ARBOR WALL STREET #2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48105', '1041 Wall St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['63647', 'Varsity Ford', 'CAR_DEALER', 'private', None, None, 'Ann Arbor', '48103', '3480 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-06-14'],
    ['74325', 'Ann Arbor Downtown Development Authority - Ashley and Washington Parking Structure', ' PAY GARAGE ', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48104', '215 W Washington', 'Washington and Ashley', 'Non-Networked', 'J1772', None, None, '3', None, 'Variable parking fee', '2022-05-05'],
    ['79282', 'First Martin', 'OFFICE_BLDG', 'private', 'Employee use only', None, 'Ann Arbor', '48104', '115 Depot St', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-09-14'],
    ['80037', 'MEADOWLARK BLDG STATION 2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48103', '3250 W Liberty Rd', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['99362', 'A & D Technology', 'OFFICE_BLDG', ' public', 'Open to public after company business hours', 'True', 'Ann Arbor', '48108', '4622 Runway Blvd', None, 'Non-Networked', 'J1772', None, None, '4', None, 'Free', '2020-12-03'],
    ['102221', 'Meijer - Tesla Supercharger', None, 'public', '24 hours daily; for Tesla use only', None, ' Ann Arbor ', '48103', '3145 Ann Arbor-Saline Road', None, 'Tesla', 'TESLA', '8', None, None, None, '$0.28 per kWh; $0.26 per minute above 60 kW and $0.13 per minute at or below 60 kW', '2021-10-11'],
    ['114460', 'Sheraton Ann Arbor Hotel - Tesla Destination', 'HOTEL', ' public', '24 hours daily; for customer use only; see front desk for access', None, 'Ann Arbor', '48108', '3200 Boardwalk Dr', None, 'Tesla Destination', 'J1772, TESLA', None, None, '4', None, 'Free', '2020-11-03'],
    ['145371', 'Roundtree Place', None, 'public', '24 hours daily', None, 'Ypsilanti ', '48197', '2539 Ellsworth Rd', None, 'Electrify America', 'CHADEMO, J1772COMBO', '6', None, None, None, None, '2022-09-07'],
    ['147501', 'MEIJER STORES 064 SALINE RD 1', None, ' public', '24 hours daily', None, 'Ann Arbor', '48108', '3145 Ann Arbor-Saline Rd', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['147555', 'U-M ANN ARBOR NCRC STATION 2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48105', '2800 Plymouth Rd', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['164341', '173 - Ann Arbor', None, ' public', '24 hours daily', None, 'Ann Arbor', '48103', '5645 Jackson Road', None, 'Greenlots', 'CHADEMO, J1772, J1772COMBO', '2', None, '4', None, None, '2022-09-26'],
    ['168052', 'The Ypsilanti Performance Space', 'OTHER_ENTERTAINMENT', 'public', '24 hours daily', 'False', 'Ypsilanti ', '48197', '218 N Adams St', None, 'Non-Networked', 'J1772', None, None, '1', None, '$1 per hour; $5 per day', '2022-08-10'],
    ['168663', 'Car & Driver - Tesla Destination', None, ' public', '24 hours daily; for customer use only; see front desk for access', None, 'Ann Arbor', '48108', '1585 Eisenhower Place', None, 'Tesla Destination', 'TESLA', None, None, '2', None, 'Free', '2020-11-03'],
    ['171786', 'U-M ANN ARBOR WALL STREET #1', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48105', '1041 Wall St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['172462', 'MEADOWLARK BLDG STATION 1', None, ' public', '24 hours daily', None, 'Ann Arbor', '48103', '3250 W Liberty Rd', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['174646', 'MEIJER STORES 064 SALINE RD 2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48108', '3145 Ann Arbor-Saline Rd', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['174657', 'U-M ANN ARBOR NCRC STATION 1', None, ' public', '24 hours daily', None, 'Ann Arbor', '48105', '2800 Plymouth Rd', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['184715', 'NOAA', 'FED_GOV', 'private ', 'Drivers must bring their own J1772 cordset for Level 1 charging', None, ' Ann Arbor ', '48108', '4840 S State Rd', None, 'Non-Networked', 'NEMA515', None, '2', None, None, None, '2021-02-22'],
    ['184845', 'EPA Ann Arbor - Station 1', 'FED_GOV', 'private', None, None, 'Ann Arbor', '48105', '2565 Plymouth Rd', None, 'Non-Networked', 'J1772', None, None, '6', None, None, '2021-02-22'],
    ['184846', 'EPA Ann Arbor - Station 2', 'FED_GOV', 'private ', 'Drivers must bring their own J1772 cordset for Level 1 charging', None, ' Ann Arbor ', '48105', '2565 Plymouth Rd', None, 'Non-Networked', 'NEMA515', None, '1', None, None, 'Free', '2021-02-22'],
    ['187890', 'HAMPTON -YPSI DTWYP #1', None, ' public', '24 hours daily', None, 'Ypsilanti ', '48197', '515 James L Hart Pkwy', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['187922', 'BMW ANN ARBOR STATION 01', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48103', '501 Auto Mall Dr', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['188119', 'Prentice Partners', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '830 Henry Street', None, 'Greenlots', 'J1772', None, None, '10', None, None, '2022-09-26'],
    ['198009', 'Hover + Greene', 'MULTI_UNIT_DWELLING', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48104', '950 Greene St', None, 'EV Connect', 'J1772', None, None, '4', None, None, '2021-11-04'],
    ['198073', 'BEEKMAN STATION 1', None, ' public', '24 hours daily', None, 'Ann Arbor', '48105', '1200 Broadway St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['199100', 'FLEET SERVICES DCFC-STATION 4', None, 'public', '24 hours daily', None, ' Ann Arbor', '48104', '301 E. Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['199101', 'FLEET SERVICES DCFC-STATION 1', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E. Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['199102', 'FLEET SERVICES DCFC-STATION 2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '301 E Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['200995', 'FLEET SERVICES DCFC-STATION 3', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['201411', 'U-M ANN ARBOR ANN 1 & 2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '1115 E Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['201412', 'U-M ANN ARBOR ANN 3', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '1101-1189 E Ann St', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['201416', 'U-M ANN ARBOR SC32', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48109', '1024 Greene St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['201417', 'U-M ANN ARBOR NC27 1 & 2', None, ' public', '24 hours daily', None, 'Ann Arbor', '48109', '1300 Murfin Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['202411', 'WASHTENAW BP 2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48108', '4975 Washtenaw Ave', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['202417', 'WASHTENAW BP 1', None, ' public', '24 hours daily', None, 'Ann Arbor', '48108', '4975 Washtenaw Ave', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['216275', 'Suburban Chevrolet', 'CAR_DEALER', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48103', '3515 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216276', 'Fourth & Washington Parking Garage', ' PARKING GARAGE', ' public', '24 hours daily', 'False', 'Ann Arbor', '48104', '123 E Washington St', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216277', 'Audi Ann Arbor', 'CAR_DEALER', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48104', '2575 S State St', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216278', 'ProQuest Employee Parking Garage', ' PARKING GARAGE', 'private', '24 hours daily', None, 'Ann Arbor', '48108', '789 E Eisenhower Pkwy', None, 'Non-Networked', 'J1772', None, None, '4', None, None, '2022-05-05'],
    ['216279', 'Staybridge Suites', 'HOTEL', 'public', '24 hours daily', 'False', ' Ann Arbor ', '48108', '3850 Research Park Dr', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-05-05'],
    ['216280', 'Mitsubishi Motor - Ann Arbor Lab', 'PARKING LOT ', ' public', '24 hours daily', 'False', 'Ann Arbor', '48108', '3735 Varsity Dr', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['223001', 'A2DDA STATION 2', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223002', 'A2DDA STATION 3', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223003', 'A2DDA STATION 1', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223004', 'A2DDA STATION 4', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223005', 'A2DDA ST 4123', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '320 Thompson St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223006', 'A2DDA STATION 4121', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '320 Thompson St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223007', 'A2DDA 500 E WASH 1', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '500 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223008', 'A2DDA 500 E WASH 2', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '500 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223009', 'A2DDA STATION 27', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '123E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223010', 'A2DDA STATION 28', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223011', 'A2DDA STATION 33', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '123E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223012', 'A2DDA STATION 22', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223013', 'A2DDA STATION 24', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223014', 'A2DDA STATION 18', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223015', 'A2DDA STATION 19', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223016', 'A2DDA STATION 20', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223017', 'A2DDA STATION 13', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '120 W Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223018', 'A2DDA STATION 17', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashely St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223019', 'A2DDA STATION 15', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223020', 'A2DDA STATION 12', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '120 W Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223021', 'A2DDA STATION 26', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223022', 'A2DDA STATION 8', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223023', 'A2DDA STATION 21', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223024', 'A2DDA STATION 16', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223025', 'A2DDA STATION 25', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223026', 'A2DDA STATION 23', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223027', 'A2DDA STATION 6', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223028', 'A2DDA STATION 31', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223029', 'A2DDA STATION 11', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223030', 'A2DDA STATION 9', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223031', 'A2DDA STATION 29', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223032', 'A2DDA STATION 32', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223033', 'A2DDA STATION 30', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223034', 'A2DDA STATION 7', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223035', 'A2DDA STATION 5', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223036', 'A2DDA STATION 10', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223038', 'A2DDA E WASH CT4K', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '123 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223039', 'A2DDA E WASH CT4K 2', None, ' public', '24 hours daily', None, 'Ann Arbor', '48104', '123 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['228549', 'Shell', None, 'public', '24 hours daily', None, ' Ann Arbor ', '48104', '2991 S State St', None, 'eVgo Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['999999', 'U-M SI 506 station #999999 (TEST RECORD)', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '715 N. University Ave', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', None, None, '10', None, None, '2018-09-26'],
]

# fmt: on


def evaluate_truth_value(val):
    return bool(val)  # check the object's truth value


def get_element(station, headers, header):
    return station[headers.index(header)]


def has_value(station, headers, header):
    element = get_element(station, headers, header)
    truth_value = evaluate_truth_value(element)
    return truth_value


def has_value_v1_p1(station, headers, header):
    return evaluate_truth_value(get_element(station, headers, header))


def has_value_v1_p2(station, headers, header):
    element = get_element(station, headers, header)
    if element:  # truth value test
        return True
    return False  # Required otherwise None is returned


def has_value_v1_p3(station, headers, header):
    if get_element(station, headers, header):
        return True
    return False  # Required otherwise None is returned


def main():
    # Instantiate a custom PrettyPrinter object
    pp = pprint.PrettyPrinter(indent=1, compact=True, width=100)

    # 3.0 Data handling: string manipulation

    headers = STATIONS[0]  # column headers
    print(f"\n3.0.1 headers (n={len(headers)})")
    stations = STATIONS[1:]  # data
    print(f"\n3.0.2 stations (n={len(stations)})")

    # Lookup index
    city_idx = headers.index("city")
    print(f"\nThis is the city index: {city_idx}")
    cities = []
    for station in stations:
         # TODO Implement
         city = station[city_idx]
         if city not in cities:
            cities.append(city)

    print(f"\n3.0.3 Cities = {cities}")

    # 3.1 STR.STRIP(), STR.LSTRIP(), STR.RSTRIP()

    ann_arbor = " Ann Arbor ".strip()  # remove leading and trailing spaces
    print(f"\n3.1.1 Ann Arbor = {ann_arbor}")

    access_code = " public".lstrip()  # remove leading space(s)
    print(f"\n3.1.2 Access code = {access_code}")

    ypsi = "Ypsilanti ".rstrip()  # remove trailing space(s)
    print(f"\n3.1.3 Ypsilanti = {ypsi}")

    si506 = "www.si506.org".strip("gorw.")  # returns "si506" #只認字母不順序
    print(f"\n3.1.4 si506 = {si506}")

    # 3.2 METHOD CHAINING

    data = " ann arbor , chelsea, dexter ,  saline, ypsilanti "

    cities = data.strip().split(", ") # remove leading and trailing spaces and split the string
    print(f"\n3.2.1 Cities = {cities}")

    # WARN: wrong order of operations
    # TODO Uncomment
    # cities = data.split(", ").strip()  # AttributeError: 'list' object has no attribute 'strip'
    #List不能用strip!!!!

    for i in range(len(cities)):
        cities[i] = cities[i].strip().title() #.title讓每個first character大寫

    print(f"\n3.2.2 Cities = {cities}")

    # 4.1 BREAK STATEMENT

    has_ypsi = False
    for station in stations:
     # TODO Implement
        if station[city_idx].strip().lower() == "ypsilanti":
            has_ypsi = True
            break  # exit loop
    print(f"\n4.1.2 Has Ypsilanti data = {has_ypsi}")

    # 4.2 CONTINUE STATEMENT

    zip_idx = headers.index("zip")
    zip_codes = []
    for station in stations:
        if station[zip_idx] not in zip_codes:
            zip_codes.append(station[zip_idx])

    print(f"\n4.2.1 Zip codes = {zip_codes}")

    outskirts = []
    for station in stations:
        zip_code = get_element(station, headers, "zip")
        city = get_element(station, headers, "city")
        street = get_element(station, headers, "street_address")
        name = get_element(station, headers, "station_name")
        access_code = get_element(station, headers, "access_code")
        if zip_code in ("48104", "48109"):
            continue  # ignore downtown Ann Arbor and U-M campus zip codes
        outskirts.append(f"{name} ({access_code}), {street}, {city}, MI {zip_code}")

    print(f"\n4.2.2 Outskirts stations (n={len(outskirts)})")
    pp.pprint(outskirts)

    # 5.0 WHILE LOOP

    print("\n5.0 while loop")
    # TODO Uncomment
    i = 0
    while i < 5:
        print(i)
        i += 1  # increment

    # for loop
    chargepoint_count = 0
    for station in stations:
        ev_network = get_element(station, headers, "ev_network")
        if ev_network.strip().lower() == "chargepoint network":
            chargepoint_count += 1

    print(f"\n5.0.1 ChargePoint network count (for loop) = {chargepoint_count}")

    # while loop
    chargepoint_count = 0
    i = 0  # Reset
    # TODO Implement while loop
    while i < len(stations):
        ev_network = get_element(station, headers, "ev_network")
        if ev_network.strip().lower() == "chargepoint network":
            chargepoint_count +=1
        i+=1
    print(f"\n5.0.2 ChargePoint network count (while loop) = {chargepoint_count}")

    # 5.1 INFINITE LOOPS

    print("\n5.1 while True")
    i = 0
    # TODO Uncomment
    while True:
        print(i, "infinite loop triggered")
        if i == 5:
            print(i, "infinite loop terminated\n")
            break  # exit the loop
        i+=1
    # 5.2 CHALLENGE 01

    ypsi_station_idx = None  # Don't default to zero
    i = 0  # reset
    # TODO Uncomment
    while True:
        city = get_element(stations[i], headers, "city")  # call function
        if city.strip().lower() == "ypsilanti":
            ypsi_station_idx = i
            break
        i += 1  # increment

    print(f"\n5.2.1 First Ypsi EV station index val = {ypsi_station_idx}")
    # assert ypsi_station_idx == 18

    # 5.3 WHILE LOOP ELSE CONDITION

    print("\n5.3 while loop with else")
    i = 0
    # TODO Uncomment
    while i < 5:
        print("I want an EV.")
        i += 1  # increment
    else:
        print("Enough said. We believe you.")

    # 5.4 WHILE LOOP AND CONDITIONAL STATEMENTS

    print("\n5.4.1 while loop if-else (increment)")
    i = 0
    # TODO Uncomment
    while i < 10:
        if i % 2 == 0:
            print(f"{i} is an even number.")
        else:
            print(f"{i} is an odd number.")
        i += 1  # increment

    print("\n5.4.2 while loop if-else (decrement)")
    i = 10
    # TODO Uncomment
    while i >= 0:
        if i % 2 == 0:
            print(f"{i} is an even number.")
        else:
            print(f"{i} is an odd number.")
        i -= 1  # decrement

    # 5.5 WHILE LOOP AND RANGE

    # print("\n5.5. while loop and range()")
    i = 0  # reset
    # TODO Uncomment
    while i in range(0, 10, 2):
        print(f"{i} is an even number.")
        i += 2  # increment by 2

    # 5.6 CHALLENGE 02

    conn_types_idx = headers.index("ev_connector_types")  # use in subscript notation below
    i = 0  # reset
    # TODO Uncomment
    while i in range(len(stations)):
         # TODO Implement
        stations[i][conn_types_idx] = stations[i][conn_types_idx].strip().split(", ")
        print(f"\n5.6.1 while loop: convert str to list (slice) = {stations[i][conn_types_idx]}")
        i+=1
    print(f"\n5.6.1 while loop: convert str to list (slice) = {stations[8][conn_types_idx]}")

    # 6.0 TRUTH VALUE TESTING

    connectors = None
    truth_value = evaluate_truth_value(connectors)  # False
    # print(f"\n6.0.1 Truth value of None = {truth_value}")

    connectors = ""
    truth_value = evaluate_truth_value(connectors)  # False
    # print(f"\n6.0.2 Truth value of empty string = {truth_value}")

    connectors = "J1772"
    truth_value = evaluate_truth_value(connectors)  # True
    # print(f"\n6.0.3 Truth value of J1772 = {truth_value}")

    connectors = []
    truth_value = evaluate_truth_value(connectors)  # False
    # print(f"\n6.0.4 Truth value of empty list = {truth_value}")

    connectors = ["CHADEMO", "J1772COMBO"]
    truth_value = evaluate_truth_value(connectors)  # True
    # print(f"\n6.0.5 Truth value of list = {truth_value}")

    count = 0
    for station in stations:
        if has_value(station, headers, "facility_type"):
            count += 1

    # print(f"\n6.0.6 Stations with facility type defined (n={len(stations)}) = {count}")

    # 6.1 Dealing with None values

    station = stations[-2]  # second to last station
    truth_value = has_value(station, headers, "facility_type")
    # print(f"\n6.1.1 has_value() = {truth_value}")

    truth_value = has_value_v1_p1(station, headers, "facility_type")
    # print(f"\n6.1.2 has_value_v1_p1() = {truth_value}")

    truth_value = has_value_v1_p2(station, headers, "facility_type")
    # print(f"\n6.1.3 has_value_v1_p2() = {truth_value}")

    truth_value = has_value_v1_p3(station, headers, "facility_type")
    # print(f"\n6.1.4 has_value_v1_p3() = {truth_value}")

    # Stations with facility type defined
    count = 0
    for station in stations:
        pass # TODO Implement

    # print(f"\n6.1.5 Stations with facility type defined (n={len(stations)}) = {count}")

    count = 0
    # TODO Uncomment
    # for station in stations:
    #     if has_value(station, headers, "facility_type"):
    #         count += 1

    # print(f"\n6.1.6 Stations with facility type defined (n={len(stations)}) = {count}")

    # 6.2 Handling ties when counting

    most_evse = []  # list accommodates multiple stations
    evse_count = 0
    # TODO Uncomment (triggers TypeError)
    # for station in stations:
    #     num = int(get_element(station, headers, "ev_level2_evse_num"))
    #     if num > evse_count:
    #         evse_count = num  # new
    #         most_evse.clear()  # clear previous leader(s)
    #         most_evse.append(station)  # new leader
    #     elif num == evse_count:
    #         most_evse.append(station)  # tie
    #     else:
    #         continue  # else condition explicit but optional

    # print(f"\n6.2.1 Most Level 2 EVSE (count={evse_count})")
    # # pp.pprint(most_evse)

    most_evse = []  # list accommodates multiple stations
    evse_count = 0
    for station in stations:
        element = get_element(station, headers, "ev_level2_evse_num")

        if not element:
            continue  # skip; not False = True

        num = int(element)
        if num > evse_count:
            evse_count = num  # new
            most_evse.clear()  # clear previous leader(s)
            most_evse.append(station)  # new leader
        elif num == evse_count:
            most_evse.append(station)  # tie
        else:
            continue  # else condition explicit but optional

    # print(f"\n6.2.2 Station(s) with most Level 2 EVSE (n={evse_count} chargers)")
    # pp.pprint(most_evse)

    # 7.2 LOGICAL AND OPERATOR

    station_evse = []
    for station in stations:
        element = get_element(station, headers, "ev_level2_evse_num")
        if element and int(element) >= 2 and int(element) <= 4:
            station_evse.append(f"{station[1]}: Level2 EVSE = {element}")

    # print(f"\n7.2.1 Stations with 2-4 Level 2 EVSE (Pythonic) (n={len(station_evse)})")
    # pp.pprint(station_evse)

    station_evse = []
    for station in stations:
        element = get_element(station, headers, "ev_level2_evse_num")
        if element and 2 <= int(element) <= 4:
            station_evse.append(f"{station[1]}: Level2 EVSE = {element}")

    # print(f"\n7.2.2 Stations with 2-4 Level 2 EVSE (Pythonic) (n={len(station_evse)})")
    # pp.pprint(station_evse)

    # 7.2 CHALLENGE 03

    # U-M charging stations
    name_idx = None  # TODO lookup index
    street_idx = None  # TODO lookup index
    um_stations = []
    for station in stations:
        pass # TODO Implement

    # print(f"\n7.2.1 U-M Greene St stations (n={len(um_stations)})")
    # pp.pprint(um_stations)

    # 7.3 LOGICAL OR OPERATOR

    a2dda_stations = []
    for station in stations:
        name = station[headers.index("station_name")].strip()
        if name.startswith("A2DDA") or name.startswith("Ann Arbor Downtown Development Authority"):
            a2dda_stations.append(station[headers.index("station_name")])

    # print(f"\n7.5 A2DDA stations (n={len(a2dda_stations)})")
    # pp.pprint(a2dda_stations)

    # 7.4 LOGICAL NOT OPERATOR

    ev_network_idx = headers.index("ev_network")

    # Count non ChargePoint network EV charging stations
    station_count = 0
    i = 0  # reset
    for i in range(len(stations)):
        if not stations[i][ev_network_idx].strip().lower() == "chargepoint network":
            station_count += 1

    # print(f"\n7.4.1 Non ChargePoint network stations count = {station_count}")

    # Alternative (!=)
    station_count = 0
    for i in range(len(stations)):
        if stations[i][ev_network_idx].strip().lower() != "chargepoint network":
            station_count += 1

    # print(f"\n7.4.2 Non ChargePoint network stations count = {station_count}")

    # 7.5 GROUPING RELATED EXPRESSIONS

    facility_type_idx = headers.index("facility_type")

    # Return list of unique "facility_type" values (case sensitive)
    facility_types = []
    for station in stations:
        if station[facility_type_idx] not in facility_types:
            facility_types.append(station[facility_type_idx])

    # print(f"\n7.5.1 facility_type unique values (n={len(facility_types)}) = {facility_types}")

    # Dedicated parking garages and lots
    parking_facilities = []
    i = 0
    while i < len(stations):
        facility_type = stations[i][facility_type_idx]
        if facility_type and (
            facility_type.strip().lower() == "parking garage"
            or facility_type.strip().lower() == "parking lot"
            or facility_type.strip().lower() == "pay garage"
        ):
            parking_facilities.append(stations[i])
        i += 1

    # print(f"\n7.5.2 Parking facilities (n={len(parking_facilities)})")
    # pp.pprint(parking_facilities)

    # Parking facilities private only
    access_code_idx = headers.index("access_code")
    parking_facilities = []
    i = 0
    while i < len(stations):
        facility_type = stations[i][facility_type_idx]
        access_code = stations[i][access_code_idx]
        if (
            facility_type
            and (
                facility_type.strip().lower() == "parking garage"
                or facility_type.strip().lower() == "parking lot"
                or facility_type.strip().lower() == "pay garage"
            )
            and access_code.strip().lower() == "private"
        ):
            parking_facilities.append(stations[i])
        i += 1

    # print(f"\n7.5.3 Private Parking facilities (n={len(parking_facilities)})")
    # pp.pprint(parking_facilities)

    parking_facilities = []
    i = 0
    while i < len(stations):
        facility_type = stations[i][facility_type_idx]
        access_code = stations[i][access_code_idx]
        if facility_type and (
            facility_type.strip().lower() == "parking_garage"
            or facility_type.strip().lower() == "parking lot"
            or facility_type.strip().lower() == "pay garage"
            and access_code.strip().lower() == "private"
        ):
            parking_facilities.append(stations[i])
        i += 1
    # print(f"\n7.5.4 ERROR: Private Parking facilities (n={len(parking_facilities)})")
    # pp.pprint(parking_facilities)

    # 7.6 CHALLENGE 04

    a2dda_stations = []
    for station in stations:
        name = None # TODO call function
        street = None # TODO call function
        # TODO Implement conditional statement block

    # print(f"\n7.6.1 A2DDA stations on Maynard St or Forrest (n={len(a2dda_stations)})")
    # pp.pprint(a2dda_stations)


if __name__ == "__main__":
    main()
