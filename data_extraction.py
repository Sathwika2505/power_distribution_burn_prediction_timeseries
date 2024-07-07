import  pandas as pd
import boto3
import io, os

def loading_data():
    access_key = os.environ.get("AWS_ACCESS_KEY_ID")
    secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    #bucket_name = os.environ.get("Bucket_Name")
    print("-acckey-----:",access_key, secret_key)
    # Initialize the S3 client
    s3 = boto3.client('s3', aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          region_name='us-east-1')
    
    bucket_name = 'deeplearning-mlops'
    file_key = 'scada_data.csv'
    
    # Download the file from S3
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        eeg_specs_data = response['Body'].read()
    
        # Read the downloaded file using Pandas
        df = pd.read_csv(io.BytesIO(eeg_specs_data))
        print(df.head())
    
    except Exception as e:
        print(f"Error downloading or reading file from S3: {e}")

        
    return df

loading_data()
