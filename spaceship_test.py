import hashlib
import spaceship
import functools

def test(test_body):
    @functools.wraps(test_body)
    def wrapper(*args, **kwargs):
        print(f'running test {test_body.__name__}...')
        test_body(args, kwargs)
        print(f'test {test_body.__name__} finished!')
    return wrapper

@test
def test_bad_angle():
    expected = 'a9bb85591bb40fddfe2bd95893777b4ab01c48648bc1c22a724dd7ddd5f3fb89'
    assert expected == hex(normalize(spaceship.bad_angle()))

@test
def test_avg_direction_angle():
    assert spaceship.avg_direction_angle(0, 360) == 180
    assert spaceship.avg_direction_angle(0, 1) == 0.5
    assert spaceship.avg_direction_angle(0, 0) == 0

@test
def test_bad_path():
    expected = 'bc89a4df27211978072cf67e4db6b3677bf3d2e28859d90622e05d0562d1b086'
    assert expected == hex(normalize(spaceship.bad_path()))

@test
def test_docking_trajectory_path():
    assert spaceship.docking_trajectory_path(1) == 1
    assert spaceship.docking_trajectory_path(2) == 1
    assert spaceship.docking_trajectory_path(3) == 2
    assert spaceship.docking_trajectory_path(12) == 144

@test
def test_bin_search_coord():
    assert spaceship.bin_search_coord([], 42) is None
    assert spaceship.bin_search_coord([42], 42)
    assert spaceship.bin_search_coord([43], 42) is False
    assert spaceship.bin_search_coord([41, 43], 42) is False
    assert spaceship.bin_search_coord([41, 42], 42)
    assert spaceship.bin_search_coord([42, 43], 42)
    assert spaceship.bin_search_coord([1, 41, 42], 42)
    assert spaceship.bin_search_coord([42, 52, 66], 42)
    assert spaceship.bin_search_coord([42, 42, 66], 42)
    assert spaceship.bin_search_coord([40, 41, 43], 42) is False

@test
def test_good_search_coord():
    expected = '03c7b1366159ce138fc110cf8eb395b7ad50091d10a96357fab9316628ea18aa'
    assert expected == hex(normalize(spaceship.good_search_coord()))

@test
def test_isort_coords():
    assert spaceship.isort_coords([]) == []
    assert spaceship.isort_coords([1]) == [1]
    assert spaceship.isort_coords([1, 2]) == [1, 2]
    assert spaceship.isort_coords([22, 1]) == [1, 22]
    assert spaceship.isort_coords([3, 5, 7]) == [3, 5, 7]
    assert spaceship.isort_coords([3, 7, 5]) == [3, 5, 7]
    assert spaceship.isort_coords([5, 3, 7]) == [3, 5, 7]
    assert spaceship.isort_coords([5, 7, 3]) == [3, 5, 7]
    assert spaceship.isort_coords([7, 3, 5]) == [3, 5, 7]
    assert spaceship.isort_coords([7, 5, 3]) == [3, 5, 7]

@test
def test_msort_coords():
    assert spaceship.msort_coords([]) == []
    assert spaceship.msort_coords([1]) == [1]
    assert spaceship.msort_coords([1, 2]) == [1, 2]
    assert spaceship.msort_coords([22, 1]) == [1, 22]
    assert spaceship.msort_coords([3, 5, 7]) == [3, 5, 7]
    assert spaceship.msort_coords([3, 7, 5]) == [3, 5, 7]
    assert spaceship.msort_coords([5, 3, 7]) == [3, 5, 7]
    assert spaceship.msort_coords([5, 7, 3]) == [3, 5, 7]
    assert spaceship.msort_coords([7, 3, 5]) == [3, 5, 7]
    assert spaceship.msort_coords([7, 5, 3]) == [3, 5, 7]


def hex(line):
    return hashlib.sha256(line.encode('utf-8')).hexdigest()


def normalize(line):
    return " ".join(line.rstrip('\n').split())

if __name__ == '__main__':
    test_bad_angle()
    test_avg_direction_angle()
    test_bad_path()
    test_docking_trajectory_path()
    test_bin_search_coord()
    test_good_search_coord()
    test_isort_coords()
    test_msort_coords()
