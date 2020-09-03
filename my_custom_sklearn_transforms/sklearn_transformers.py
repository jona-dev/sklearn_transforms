from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')
    
#--------------------------------------------------------------    
# Implementación de clase para agregar columna eliminada
#--------------------------------------------------------------
class AddColumnObjetivo:
    
    def __init__(self, columns = None):
        self.data=self

    def fit(self, X, y=None):
        return self
    
    def transform(self, X,Y):
        # Primero copiamos el dataframe de datos de entrada 'X'
        df = X.copy()
        df2= Y.copy()
       
        df['OBJETIVO'] = df2['OBJETIVO']
        
        #limpio sus indices, por las dudas
        df.reset_index(inplace=True, drop=True)
        
        return df
