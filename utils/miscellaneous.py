def update_stats(stats, epoch, train_loss, test_loss, train_auc, test_auc):
    print(
        '\nEpoch: {0} | Training loss: {1:.4f} | Testing loss: {2:.4f} | Training AUC: {3:.4f} | Testing AUC: {4:.4f}'.format(
            epoch, train_loss, test_loss, train_auc, test_auc
        )
    )
    stats['epoch'].append(epoch)
    stats['training_loss'].append(train_loss)
    stats['testing_loss'].append(test_loss)
    stats['training_auc'].append(train_auc)
    stats['testing_auc'].append(test_auc)
    return
