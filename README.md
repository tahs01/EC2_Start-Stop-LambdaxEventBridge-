### **1. Create the Lambda Function**

### **Step 1: Set Up the Lambda Function**

1. **Go to AWS Lambda Console**:
    - Navigate to the [AWS Lambda console](https://console.aws.amazon.com/lambda/).
    - Click **Create function**.
    - Select **Author from scratch**.
    - Name your function, e.g., `StartStopEC2Instance`.
    - Set the runtime to `Python 3.x`.

### **Step 2: Add the Python Script**

### **Step 3: Deploy the Lambda Function**

- Paste the above code into the Lambda console editor.
- Click **Deploy** to save the function.

### **2. Set Up EventBridge Rules**

You can create EventBridge rules to trigger the Lambda function at specific times.

### **Step 1: Create Start/Stop Rules**

1. **Go to Amazon EventBridge Console**:
    - Navigate to the [Amazon EventBridge console](https://console.aws.amazon.com/events/).
    - Click **Create rule**.
2. **Define a Start Rule**:
    - Name the rule, e.g., `StartEC2Instances`.
    - **Event Source**: Choose `Schedule`.
    - **Schedule Expression**: Define a cron expression for when you want to start the instances (e.g., `cron(0 8 * * ? *)` for 8 AM UTC).
    - **Select Target**: Choose **Lambda function** and select your Lambda function.
    - **Configure Input**:
        - In the **Configure input** section, select **Constant (JSON text)**.
            
3. **Define a Stop Rule**:
    - Repeat the steps to create another rule to stop the instances. Name it, e.g., `StopEC2Instances`.
    - Define the schedule (e.g., `cron(0 18 * * ? *)` for 6 PM UTC).
    - Set the action to `"stop"` in the JSON input.

### **3. Summary**

- **Lambda Function**: The Lambda function uses the EC2 client to start or stop instances based on the event input.
- **EventBridge**: The rules are set to trigger the Lambda function at specified times with the necessary parameters.
