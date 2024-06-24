import torch
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import matplotlib.pyplot as plt
import copy

# Image loading and preprocessing
def load_image(image_path, max_size=400, shape=None):
    image = Image.open(image_path).convert('RGB')
    
    # Resize the image
    if max(image.size) > max_size:
        size = max_size
    else:
        size = max(image.size)
        
    if shape is not None:
        size = shape
    
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    
    image = transform(image).unsqueeze(0)
    return image

# Convert tensor to image
def im_convert(tensor):
    image = tensor.clone().detach().cpu().numpy().squeeze(0)
    image = image.transpose(1, 2, 0)
    image = image.clip(0, 255).astype('uint8')
    return image

content_image = load_image('path_to_content_image.jpg').to(device)
style_image = load_image('path_to_style_image.jpg', shape=content_image.shape[-2:]).to(device)

plt.figure()
plt.imshow(im_convert(content_image))
plt.figure()
plt.imshow(im_convert(style_image))

# Define the Model
class VGG(nn.Module):
    def __init__(self):
        super(VGG, self).__init__()
        self.chosen_features = ['0', '5', '10', '19', '28']
        self.model = models.vgg19(pretrained=True).features[:29]
        
    def forward(self, x):
        features = []
        for layer_num, layer in enumerate(self.model):
            x = layer(x)
            if str(layer_num) in self.chosen_features:
                features.append(x)
        return features
      
    def content_loss(gen_features, content_features):
        return F.mse_loss(gen_features, content_features)

    def gram_matrix(tensor):
        _, d, h, w = tensor.size()
        tensor = tensor.view(d, h * w)
        gram = torch.mm(tensor, tensor.t())
        return gram / (d * h * w)

    def style_loss(gen_features, style_grams):
        style_loss = 0
        for gen, style in zip(gen_features, style_grams):
            gen_gram = gram_matrix(gen)
            style_loss += F.mse_loss(gen_gram, style)
        return style_loss

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = VGG().to(device).eval()

# Extract features
content_features = model(content_image)
style_features = model(style_image)
style_grams = [gram_matrix(feature) for feature in style_features]

# Initialize generated image
generated_image = content_image.clone().requires_grad_(True)

# Hyperparameters
total_steps = 6000
learning_rate = 0.003
alpha = 1  # content weight
beta = 0.01  # style weight

optimizer = optim.Adam([generated_image], lr=learning_rate)

for step in range(total_steps):
    generated_features = model(generated_image)
    c_loss = content_loss(generated_features[1], content_features[1])
    s_loss = style_loss(generated_features, style_grams)
    total_loss = alpha * c_loss + beta * s_loss
    
    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()
    
    if step % 500 == 0:
        print(f"Step [{step}/{total_steps}], Content Loss: {c_loss.item():.4f}, Style Loss: {s_loss.item():.4f}")
        plt.imshow(im_convert(generated_image))
        plt.show()

# Save the final generated image
final_image = im_convert(generated_image)
plt.imshow(final_image)
plt.imsave('generated_image.jpg', final_image)
plt.show()
