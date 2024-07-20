require 'openssl'
require 'base64'

class CybersecurityModule
  def initialize(api_key)
    @api_key = api_key
  end

  def encrypt_data(data)
    cipher = OpenSSL::Cipher.new('AES-256-CBC')
    cipher.encrypt
    cipher.key = Base64.decode64(@api_key)
    iv = cipher.random_iv
    encrypted_data = cipher.update(data) + cipher.final
    return { encrypted_data: Base64.encode64(encrypted_data), iv: Base64.encode64(iv) }
  end

  def decrypt_data(encrypted_data, iv)
    cipher = OpenSSL::Cipher.new('AES-256-CBC')
    cipher.decrypt
    cipher.key = Base64.decode64(@api_key)
    cipher.iv = Base64.decode64(iv)
    decrypted_data = cipher.update(Base64.decode64(encrypted_data)) + cipher.final
    return decrypted_data
  end
end

api_key = 'YOUR_API_KEY'
cybersecurity_module = CybersecurityModule.new(api_key)

data = 'This is a secret message.'
encrypted_data = cybersecurity_module.encrypt_data(data)
decrypted_data = cybersecurity_module.decrypt_data(encrypted_data[:encrypted_data], encrypted_data[:iv])

puts "Original data: #{data}"
puts "Encrypted data: #{encrypted_data[:encrypted_data]}"
puts "Decrypted data: #{decrypted_data}"
