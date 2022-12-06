# We are going to create a tls_private_key
resource "tls_private_key" "aws_key" {
    algorithm   = "RSA"
    rsa_bits    = 4096
}

# This creates a file to the ansible route for the private key
resource "local_file" "ec2key" {
    content     = tls_private_key.aws_key.private_key_pem
    filename    = "../ansible/ec2key"
}

# This will write the public key to aws
resource "aws_key_pair" "aws_ec2_key" {
    key_name        = "ec2key"
    public_key      = tls_private_key.aws_key.public_key_openssh
}

resource "aws_instance" "ec2_streamlit" {
    ami = "ami-0574da719dca65348" # Ubuntu image
    instance_type = "t2.micro"

    key_name                    = aws_key_pair.aws_ec2_key.key_name
    vpc_security_group_ids      = [aws_security_group.project_security_group.id]
    user_data                   =  file ("user_data.sh")

    tags = {
        Name    = "ec2_streamlitapp"
        app     = "streamlit"
    }

}