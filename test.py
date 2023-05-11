from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1(self):
        self.assertEqual(solution([2,7,11,15],9), [0,1])
    
    def test_2(self):
        self.assertEqual(solution([3,2,4],6), [1,2])

    def test_3(self):
        self.assertEqual(solution([3,3],6),  [0,1]) 

    def test_4(self):
        self.assertEqual(solution([0,8,9,7],7),  [0,3]) 



if __name__ == "__main__":
    main()

