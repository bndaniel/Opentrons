from opentrons import protocol_api

metadata = {
    'apiLevel': '2.8',
    'protocolName': 'Pooling Feb 4, 2021',
    'author': 'Aditya R. Jangid <aditya.jangid@gmail.com>'}


def run(protocol=protocol_api.ProtocolContext):

    protocol.max_speeds['X'] = 400
    protocol.max_speeds['Y'] = 400
    protocol.max_speeds['A'] = 200

    rack = '5.0mlmacrotube5_15_tuberack_5000ul'
    well96 = 'corning_96_wellplate_360ul_flat'
    tiprack = 'opentrons_96_tiprack_300ul'

    sample_holder_1 = protocol.load_labware(rack, 1)
    sample_holder_4 = protocol.load_labware(rack, 4)
    sample_holder_7 = protocol.load_labware(rack, 7)
    sample_holder_10 = protocol.load_labware(rack, 10)
    sample_holder_2 = protocol.load_labware(rack, 2)
    sample_holder_5 = protocol.load_labware(rack, 5)
    sample_holder_8 = protocol.load_labware(rack, 8)
    sample_holder_11 = protocol.load_labware(rack, 11)

    pool_of_5_plate = protocol.load_labware(well96, 9)
    tiprack200_1 = protocol.load_labware(tiprack, 3)
    tiprack200_2 = protocol.load_labware(tiprack, 6)

    p50 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack200_1, tiprack200_2])

    sample_plate_values = ['A1', 'A2', 'A3', 'A4', 'A5',
                           'B1', 'B2', 'B3', 'B4', 'B5',
                           'C1', 'C2', 'C3', 'C4', 'C5']
                           

    dest = ['C1', 'C1', 'C1', 'C1', 'C1',
            'C2', 'C2', 'C2', 'C2', 'C2',
            'C3', 'C3', 'C3', 'C3', 'C3',
            'C4', 'C4', 'C4', 'C4', 'C4',
            'C5', 'C5', 'C5', 'C5', 'C5',
            'C6', 'C6', 'C6', 'C6', 'C6',
            'C7', 'C7', 'C7', 'C7', 'C7',
            'C8', 'C8', 'C8', 'C8', 'C8',
            'C9', 'C9', 'C9', 'C9', 'C9',
            'C10', 'C10', 'C10', 'C10', 'C10',
            'C11', 'C11', 'C11', 'C11', 'C11',
            'C12', 'C12', 'C12', 'C12', 'C12',
            'D1', 'D1', 'D1', 'D1', 'D1',
            'D2', 'D2', 'D2', 'D2', 'D2',
            'D3', 'D3', 'D3', 'D3', 'D3',
            'D4', 'D4', 'D4', 'D4', 'D4',
            'D5', 'D5', 'D5', 'D5', 'D5',
            'D6', 'D6', 'D6', 'D6', 'D6',
            'D7', 'D7', 'D7', 'D7', 'D7',
            'D8', 'D8', 'D8', 'D8', 'D8',
            'D9', 'D9', 'D9', 'D9', 'D9',
            'D10', 'D10', 'D10', 'D10', 'D10',
            'D11', 'D11', 'D11', 'D11', 'D11',
            'D12', 'D12', 'D12', 'D12', 'D12']

    mixing_counter = 1
    current_tip_number = 0
    current_sample_well_value = 0
    tube_rack_number = 1

    p50.flow_rate.aspirate = 50
    p50.flow_rate.dispense = 50

    for destination in dest:

        if current_sample_well_value >= 15:
            current_sample_well_value = 0
            tube_rack_number += 1

        if tube_rack_number == 1:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_10[sample_plate_values[current_sample_well_value]].bottom(22))
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()
            
        if tube_rack_number == 2:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_7[sample_plate_values[current_sample_well_value]].bottom(22))           
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()

        if tube_rack_number == 3:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_4[sample_plate_values[current_sample_well_value]].bottom(22))           
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()

        if tube_rack_number == 4:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_1[sample_plate_values[current_sample_well_value]].bottom(22))
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()

        if tube_rack_number == 5:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_11[sample_plate_values[current_sample_well_value]].bottom(22))
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()

        if tube_rack_number == 6:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_8[sample_plate_values[current_sample_well_value]].bottom(22))
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()

        if tube_rack_number == 7:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_5[sample_plate_values[current_sample_well_value]].bottom(22))
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()

        if tube_rack_number == 8:
            p50.pick_up_tip()
            current_tip_number += 1
            p50.aspirate(35, sample_holder_2[sample_plate_values[current_sample_well_value]].bottom(22))
            current_sample_well_value += 1
            p50.dispense(35, pool_of_5_plate[destination])
            if mixing_counter % 5 == 0:
                p50.mix(1, 50, pool_of_5_plate[destination])
            mixing_counter += 1
            p50.drop_tip()
  
 