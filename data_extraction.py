import  pandas as pd
import boto3
import io

def loading_data():
    s3 = boto3.client('s3')

    bucket_name = 'deeplearning-mlops-demo'
    file_key = 'scada_2data.csv'
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    eeg_specs_data = response['Body'].read()

    # Read the downloaded file using Pandas
    df = pd.read_csv(io.BytesIO(eeg_specs_data))
    df.index = pd.to_datetime(df.index)
    # Now you can work with the DataFrame 'df'
    print(df)
        
    return df

loading_data()
