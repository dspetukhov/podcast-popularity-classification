import torch
from sklearn.metrics import roc_auc_score


def training(model, optimizer, criterion, dataloader, device='cpu'):
    losses, y_true, y_score = [], [], []
    #
    model.train()
    for X, Y in dataloader:
        X, Y = X.to(device), Y.to(device, dtype=torch.float32)
        #
        output = model(X)
        loss = criterion(output.view(1), Y)
        #
        losses.append(loss.item())
        y_true.append(Y.item())
        y_score.append(torch.sigmoid(output).item())
        #
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return torch.tensor(losses).mean(), roc_auc_score(y_true, y_score)


def testing(model, optimizer, criterion, dataloader, device='cpu'):
    losses, y_true, y_score = [], [], []
    #
    model.eval()
    with torch.inference_mode():
        for X, Y in dataloader:
            X, Y = X.to(device), Y.to(device, dtype=torch.float32)
            #
            output = model(X)
            loss = criterion(output.view(1), Y)
            #
            losses.append(loss.item())
            y_true.append(Y.item())
            y_score.append(torch.sigmoid(output).item())
    #
    return torch.tensor(losses).mean(), roc_auc_score(y_true, y_score)