from opentrons import protocol_api



metadata = {

    'apiLevel': '2.8',

    'protocolName': 'Transfer Single Channel',

    'author': 'Aditya R. Jangid <aditya.jangid@gmail.com>'}





def run(protocol=protocol_api.ProtocolContext):

    rack = '5.0mlmacrotube5_15_tuberack_5000ul'

    tiprack = 'opentrons_96_tiprack_300ul'

    qPCR_plate = 'biorad_96_wellplate_200ul_pcr'



    sample_holder_1 = protocol.load_labware(rack, 1)

    sample_holder_4 = protocol.load_labware(rack, 4)

    sample_holder_7 = protocol.load_labware(rack, 7)

    sample_holder_10 = protocol.load_labware(rack, 10)

    sample_holder_2 = protocol.load_labware(rack, 2)

    sample_holder_5 = protocol.load_labware(rack, 5)

    sample_holder_8 = protocol.load_labware(rack, 8)

    sample_holder_11 = protocol.load_labware(rack, 11)



    tiprack20_1 = protocol.load_labware(tiprack, 3)

    tiprack20_2 = protocol.load_labware(tiprack, 6)



    qCPR = protocol.load_labware(qPCR_plate, 9)



    p20_single = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack20_1])



    sample_plate_values = ['A1', 'A2', 'A3', 'A4', 'A5',

                           'B1', 'B2', 'B3', 'B4', 'B5',

                           'C1', 'C2', 'C3', 'C4', 'C5']



    dest = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12',

            'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12',

            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12',

            'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12',

            'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12',

            'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',

            'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12',

            'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12']



    current_sample_well_value = 0

    tube_rack_number = 1



    p20_single.flow_rate.aspirate = 7

    p20_single.flow_rate.dispense = 7



    for destination in dest:



        if current_sample_well_value >= 15:

            current_sample_well_value = 0

            tube_rack_number += 1



        if tube_rack_number == 1:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_10[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()



        if tube_rack_number == 2:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_7[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()



        if tube_rack_number == 3:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_4[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()



        if tube_rack_number == 4:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_1[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()



        if tube_rack_number == 5:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_11[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()



        if tube_rack_number == 6:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_8[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()



        if tube_rack_number == 7:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_5[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()



        if tube_rack_number == 8:

            p20_single.pick_up_tip()

            p20_single.aspirate(14, sample_holder_2[sample_plate_values[current_sample_well_value]])

            current_sample_well_value += 1

            p20_single.dispense(14, qCPR[destination])

            p20_single.drop_tip()

