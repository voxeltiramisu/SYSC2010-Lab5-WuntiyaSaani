import unittest
from Lab5_Classes import*






class Testcases(unittest.TestCase):










    ecg = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2]

    def setUp(self):
        self.num = Numbers()
        self.ecgObj = ECG()
     
    def test_factorial_1(self):
        x = self.num.factorial(4)

        self.assertEqual(x , 24)
    
    def test_factorial_2(self):
        x = self.num.factorial(1)
        self.assertEqual(x , 1)
        
    def test_factorial_3(self):
        x = self.num.factorial(3)
        self.assertEqual(x , 6)

    def test_addtoSum_1(self): 
        self.num.addToSum(4)
        self.num.addToSum(4)
        x = self.num.addToSum(4)
        self.assertEqual(x , 12)
    
    def test_subtractFromSum_1(self):
        self.num.subtractFromSum(2)
        self.num.subtractFromSum(2)
        x = self.num.subtractFromSum(2)
        self.assertEqual(x , -6)

    def test_stringOfNumber_1(self):
        x = self.num.stringOfNumber(4)
        self.assertEqual(x , "four")




class TestECG(unittest.TestCase):
    
    def setUp(self):
        self.num = Numbers()
        self.ecgObj = ECG()

    def test_detect_peaks1(self):
        ecg = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2]
        x = self.ecgObj.detect_peaks(ecg,1)
        self.assertEqual(x , [2, 5])

    def test_detect_peaks2(self):
        ecg = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2]
        x = self.ecgObj.detect_peaks(ecg,3)
        self.assertEqual(x , [])

    def test_remove_baseline1(self):
        ecg = [2,2,2,2,2]
        x = self.ecgObj.remove_baseline(ecg)
        self.assertEqual(x , [0,0,0,0,0])

    def test_normalize1(self):
        ecg = [10,30,100,60,20,10]
        x = self.ecgObj.normalize(ecg)
        self.assertEqual(x , [0.1,0.3,1,0.6,0.2,0.1])

    def test_normalize2(self):
        ecg = [0,0,0,0,0]
        x = self.ecgObj.normalize(ecg)
        self.assertEqual(x , [0,0,0,0,0])

    def test_rr_intervals1(self):
        ecg = [2,3,6,8]
        x = self.ecgObj.rr_intervals(ecg, 100)
        self.assertEqual(x , [0.01,0.03,0.02])

    def test_is_signal_valid1(self):
        ecg = [2,3,6,8]
        x = self.ecgObj.is_signal_valid(ecg)
        self.assertEqual(x ,True)
        
    def test_is_signal_valid2(self):
        ecg = []
        x = self.ecgObj.is_signal_valid(ecg)
        self.assertEqual(x ,False)

    def test_is_signal_valid3(self):
        ecg = [2.0,3.0,6,8]
        x = self.ecgObj.is_signal_valid(ecg)
        self.assertEqual(x ,True)
        
    def test_is_signal_valid4(self):
        ecg = [2.0,"3.0",6,8]
        x = self.ecgObj.is_signal_valid(ecg)
        self.assertEqual(x ,False)
        

    def test_heart_rate1(self):
        peaks = [100, 300, 500, 700]
        fs = 250
        x = self.ecgObj.heart_rate(peaks,fs)
        self.assertEqual(round(x) ,75) #It prints 74.9999999999999999 unless rounded

    def test_heart_rate2(self):
        peaks = []
        fs = 250
        x = self.ecgObj.heart_rate(peaks,fs)
        self.assertEqual(x ,None)
    
    def test_heart_rate3(self):
        peaks = [100]
        fs = 250
        x = self.ecgObj.heart_rate(peaks,fs)
        self.assertEqual(x ,None)
        

if __name__ == "__main__":
    unittest.main()