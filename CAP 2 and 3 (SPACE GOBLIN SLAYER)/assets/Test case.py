import unittest
from Space import Ship
from Space import Enemy

class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship(0, 0)

    def test_init(self):
        self.assertEqual(self.ship.x, 0)
        self.assertEqual(self.ship.y, 0)
        self.assertEqual(self.ship.health, 100)
    
    def test_move(self):
        # Accessing ship attributes
        initial_x = self.ship.x
        initial_y = self.ship.y
    
    def test_move_left(self):
        initial_x = self.ship.x
        self.ship.move_left()
        self.assertEqual(self.ship.x, initial_x - 1)

    def test_move_right(self):
        initial_x = self.ship.x
        self.ship.move_right()
        self.assertEqual(self.ship.x, initial_x + 1)

    def test_take_damage(self):
        initial_health = self.ship.health
        damage_amount = 20
        self.ship.take_damage(damage_amount)
        self.assertEqual(self.ship.health, initial_health - damage_amount)

class TestEnemy(unittest.TestCase):
    def test_enemy_creation(self):
        # Test the creation of an enemy instance
        enemy = Enemy(100, 200, "red", health=50)
        self.assertEqual(enemy.x, 100)
        self.assertEqual(enemy.y, 200)
        self.assertEqual(enemy.health, 50)
        self.assertIsNotNone(enemy.ship_img)
        self.assertIsNotNone(enemy.laser_img)
        self.assertIsNotNone(enemy.mask)

    def test_enemy_movement(self):
        # Test the movement of an enemy
        enemy = Enemy(100, 200, "red")
        initial_y = enemy.y
        enemy.move(5)
        self.assertEqual(enemy.y, initial_y + 5)


if __name__ == '__main__':
    unittest.main()
