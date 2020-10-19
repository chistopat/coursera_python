import solution


def test():
    car = solution.Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
    assert car.brand == 'Bugatti Veyron'
    assert car.carrying == 0.312
    assert car.passenger_seats_count == 2
    assert car.get_photo_file_ext() == '.png'

    truck = solution.Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
    assert truck.brand == 'Nissan'
    assert truck.car_type == 'truck'
    assert truck.photo_file_name == 'nissan.jpeg'
    assert truck.carrying == 1.5
    assert truck.get_photo_file_ext() == '.jpeg'
    assert truck.body_length == 3.92
    assert truck.body_width == 2.09
    assert truck.body_height == 1.87

    truck = solution.Truck('Nissan', 'nissan.jpeg', '1.5', 'WxJXL')
    assert truck.brand == 'Nissan'
    assert truck.car_type == 'truck'
    assert truck.photo_file_name == 'nissan.jpeg'
    assert truck.carrying == 1.5
    assert truck.get_photo_file_ext() == '.jpeg'
    assert truck.body_length == 0
    assert truck.body_width == 0
    assert truck.body_height == 0

    spec_machine = solution.SpecMachine('Komatsu-D355', 'd355.jpg', '93',
                               'pipelayer specs')

    assert spec_machine.brand == 'Komatsu-D355'
    assert spec_machine.extra == 'pipelayer specs'
    assert spec_machine.carrying == 93
    assert spec_machine.get_photo_file_ext() == '.jpg'
    assert spec_machine.car_type == 'spec_machine'
    assert spec_machine.photo_file_name == 'd355.jpg'
    expected = solution.get_car_list('invalid.csv')
    assert expected == []
if __name__ == '__main__':
    test()
