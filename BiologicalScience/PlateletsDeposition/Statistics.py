import numpy as np
from abcpy.statistics import Statistics
        
class DepositionStatistics(Statistics):
    """
    This class implements the statistics function from the Statistics protocol. This 
    extracts the statistics following Hakkarainen et. al. [1] from the multivariate timesereis 
    generated by solving Lorenz 95 odes.
    
    [1] J. Hakkarainen, A. Ilin, A. Solonen, M. Laine, H. Haario, J. Tamminen, E. Oja, and 
    H. Järvinen. On closure parameter estimation in chaotic systems. Nonlinear Processes 
    in Geophysics, 19(1):127–143, Feb. 2012.
    """

    def __init__(self, degree = 2, cross = True):
        self.degree = degree                
        self.cross = cross
        
    def statistics(self, data):      
        num_element = len(data)
        result = np.zeros(shape=(num_element,24))
        # Compute statistics
        for ind_element in range(0,num_element):
            data_ind_element = np.array(data[ind_element])
            # Mean             
            s1 = np.mean(data_ind_element,axis = 0)[1:]
            # Variance
            s2 = np.var(data_ind_element, axis = 0)[1:]
            ## Auto Covariance with lag 1
            s3 = np.zeros(shape=(data_ind_element.shape[1]-1,))
            for ind in range(data_ind_element.shape[1]-1):
                s3[ind] = self._auto_covariance(data_ind_element[:,ind+1], lag = 1) 
            ## Index of combination 
            II = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
            ## Correlation within a pair of variables
            s4 = np.zeros(shape=(len(II),))
            for ind in range(len(II)):            
                ind1, ind2 = II[ind][0], II[ind][1] 
                s4[ind] = (np.mean(data_ind_element[:,ind1]*data_ind_element[:,ind2])\
                    - np.mean(data_ind_element[:,ind1])*np.mean(data_ind_element[:,ind2]))\
                    /np.sqrt(np.var(data_ind_element[:,ind1])*np.var(data_ind_element[:,ind2]))
            ## Cross-Correlation for time lag 1 within a pair of variables
            s5 = np.zeros(shape=(len(II),))
            for ind in range(len(II)):
                ind1, ind2 = II[ind][0], II[ind][1] 
                s5[ind] = self._cross_covariance(data_ind_element[:,ind1],data_ind_element[:,ind2])
               
            result[ind_element,:] = np.concatenate((s1, s2, s3, s4, s5))
            
        # Expand the data with polynomial expansion            
        result = self._polynomial_expansion(result) 
                
        return np.array(result)
    
    def _cross_covariance(self, x, y):
        """ Computes cross-covariance between x and y 
        
        Parameters
        ----------
        x: numpy.ndarray
            Vector of real numbers.
        y: numpy.ndarray
            Vector of real numbers.
        
        Returns
        -------
        numpy.ndarray
            Cross-covariance calculated between x and y.
        """
        result = (np.mean(np.insert(x,0,1)*np.insert(y,-1,1))-np.mean(np.insert(x,0,1))*np.mean(np.insert(y,-1,1)))\
        /np.sqrt(np.var(np.insert(x,0,1))*np.var(np.insert(y,-1,1)))
        
        return result
        
        
    def _auto_covariance(self, x, lag = 1):
        """
        Calculate the autocovarriance coefficient of x with lag k.

        Parameters
        ----------
        x: numpy.ndarray
            Vector of real numbers.
        k: integer
            Time-lag.
        
        Returns
        -------
        numpy.ndarray
            Returns the auto-covariance of x with time-lag k.
        """

        N = x.shape[0]
        x_mean = np.average(x)

        autoCov = 0.0
        for ind in range(0, N-lag):
            autoCov += (x[ind+lag]-x_mean)*(x[ind]-x_mean)
        return ((1/(N-1))*autoCov)/np.var(x)
        
class DepositionIdentityStatistics(Statistics):
    """
    This class implements the statistics function from the Statistics protocol. This 
    extracts the statistics following Hakkarainen et. al. [1] from the multivariate timesereis 
    generated by solving Lorenz 95 odes.
    
    [1] J. Hakkarainen, A. Ilin, A. Solonen, M. Laine, H. Haario, J. Tamminen, E. Oja, and 
    H. Järvinen. On closure parameter estimation in chaotic systems. Nonlinear Processes 
    in Geophysics, 19(1):127–143, Feb. 2012.
    """

    def __init__(self, degree = 2, cross = True):
        self.degree = degree                
        self.cross = cross
        
    def statistics(self, data):      
                        
        return data[0]   
        
class DepositionStatisticsCombined(Statistics):
    """
    This class implements the statistics function from the Statistics protocol. This 
    extracts the statistics following Hakkarainen et. al. [1] from the multivariate timesereis 
    generated by solving Lorenz 95 odes.
    
    [1] J. Hakkarainen, A. Ilin, A. Solonen, M. Laine, H. Haario, J. Tamminen, E. Oja, and 
    H. Järvinen. On closure parameter estimation in chaotic systems. Nonlinear Processes 
    in Geophysics, 19(1):127–143, Feb. 2012.
    """

    def __init__(self, degree = 2, cross = True):
        self.degree = degree                
        self.cross = cross
        
    def statistics(self, data):      
        num_element = len(data)
        result = np.zeros(shape=(num_element,24))
        # Compute statistics
        for ind_element in range(0,num_element):
            data_ind_element = np.array(data[ind_element])
            # Mean             
            s1 = np.mean(data_ind_element,axis = 0)[1:]
            # Variance
            s2 = np.var(data_ind_element, axis = 0)[1:]
            ## Auto Covariance with lag 1
            s3 = np.zeros(shape=(data_ind_element.shape[1]-1,))
            for ind in range(data_ind_element.shape[1]-1):
                s3[ind] = self._auto_covariance(data_ind_element[:,ind+1], lag = 1) 
            ## Index of combination 
            II = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
            ## Correlation within a pair of variables
            s4 = np.zeros(shape=(len(II),))
            for ind in range(len(II)):            
                ind1, ind2 = II[ind][0], II[ind][1] 
                s4[ind] = (np.mean(data_ind_element[:,ind1]*data_ind_element[:,ind2])\
                    - np.mean(data_ind_element[:,ind1])*np.mean(data_ind_element[:,ind2]))\
                    /np.sqrt(np.var(data_ind_element[:,ind1])*np.var(data_ind_element[:,ind2]))
            ## Cross-Correlation for time lag 1 within a pair of variables
            s5 = np.zeros(shape=(len(II),))
            for ind in range(len(II)):
                ind1, ind2 = II[ind][0], II[ind][1] 
                s5[ind] = self._cross_covariance(data_ind_element[:,ind1],data_ind_element[:,ind2])
               
            result[ind_element,:] = np.concatenate((s1, s2, s3, s4, s5))
            
        # Expand the data with polynomial expansion            
        result = self._polynomial_expansion(result) 
                
        return [result, data[0]]
    
    def _cross_covariance(self, x, y):
        """ Computes cross-covariance between x and y 
        
        Parameters
        ----------
        x: numpy.ndarray
            Vector of real numbers.
        y: numpy.ndarray
            Vector of real numbers.
        
        Returns
        -------
        numpy.ndarray
            Cross-covariance calculated between x and y.
        """
        result = (np.mean(np.insert(x,0,1)*np.insert(y,-1,1))-np.mean(np.insert(x,0,1))*np.mean(np.insert(y,-1,1)))\
        /np.sqrt(np.var(np.insert(x,0,1))*np.var(np.insert(y,-1,1)))
        
        return result
        
        
    def _auto_covariance(self, x, lag = 1):
        """
        Calculate the autocovarriance coefficient of x with lag k.

        Parameters
        ----------
        x: numpy.ndarray
            Vector of real numbers.
        k: integer
            Time-lag.
        
        Returns
        -------
        numpy.ndarray
            Returns the auto-covariance of x with time-lag k.
        """

        N = x.shape[0]
        x_mean = np.average(x)

        autoCov = 0.0
        for ind in range(0, N-lag):
            autoCov += (x[ind+lag]-x_mean)*(x[ind]-x_mean)
        return ((1/(N-1))*autoCov)/np.var(x)
