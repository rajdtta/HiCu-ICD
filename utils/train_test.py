import torch
import numpy as np
from datetime import datetime
from utils.utils import all_metrics, print_metrics


def train(args, model, optimizer, scheduler, epoch, gpu, data_loader, cur_depth):
    print(f"EPOCH {epoch} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    losses = []
    model.train()

    # loader
    data_iter = iter(data_loader)
    num_iter = len(data_loader)
    for i in range(num_iter):
        print(f"Batch {i}/{num_iter}")
        if args.model.find("bert") != -1 or args.model.find("xlnet") != -1 or args.model.find("longformer") != -1:

            inputs_id, segments, masks, labels = next(data_iter)

            curr_depth = np.array(labels[cur_depth]) if isinstance(labels[cur_depth], list) else labels[cur_depth]

            inputs_id, segments, masks, labels = torch.LongTensor(inputs_id), torch.LongTensor(segments), \
                torch.LongTensor(masks), torch.FloatTensor(curr_depth)

            if gpu[0] >= 0:
                if torch.backends.mps.is_available():
                    inputs_id, segments, masks, labels = inputs_id.to(torch.device('mps')), segments.to(
                        torch.device('mps')), \
                        masks.to(torch.device('mps')), labels.to(torch.device('mps'))
                else:
                    inputs_id, segments, masks, labels = inputs_id.cuda(), segments.cuda(), \
                        masks.cuda(), labels.cuda()

            output, loss, _, _ = model(inputs_id, segments, masks, labels)
        else:
            inputs_id, labels, text_inputs = next(data_iter)

            curr_depth = np.array(labels[cur_depth]) if isinstance(labels[cur_depth], list) else labels[cur_depth]

            inputs_id, labels = torch.LongTensor(inputs_id), torch.FloatTensor(curr_depth)

            if gpu[0] >= 0:
                if torch.backends.mps.is_available():
                    inputs_id, labels, text_inputs = inputs_id.to(torch.device('mps')), labels.to(
                        torch.device('mps')), text_inputs.to(torch.device('mps'))
                else:
                    inputs_id, labels, text_inputs = inputs_id.cuda(), labels.cuda(), text_inputs.cuda()

            output, loss, _, _ = model(inputs_id, labels, text_inputs)

        if len(gpu) > 1:
            loss = loss.mean()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if args.model.find("bert") != -1:
            scheduler.step()

        losses.append(loss.item())

    return losses


def test(args, model, data_path, fold, gpu, dicts, data_loader, cur_depth=4):
    filename = data_path.replace('train', fold)
    print('file for evaluation: %s' % filename)

    y, yhat, yhat_raw, hids, losses = [], [], [], [], []

    model.eval()

    # loader
    data_iter = iter(data_loader)
    num_iter = len(data_loader)
    for i in range(num_iter):
        print(f"Batch {i}/{num_iter}")
        with torch.no_grad():

            if args.model.find("bert") != -1 or args.model.find("xlnet") != -1 or args.model.find("longformer") != -1:
                inputs_id, segments, masks, labels = next(data_iter)

                curr_depth = np.array(labels[cur_depth]) if isinstance(labels[cur_depth], list) else labels[cur_depth]

                inputs_id, segments, masks, labels = torch.LongTensor(inputs_id), torch.LongTensor(segments), \
                    torch.LongTensor(masks), torch.FloatTensor(curr_depth)

                if gpu[0] >= 0:
                    if torch.backends.mps.is_available():
                        inputs_id, segments, masks, labels = inputs_id.to(torch.device('mps')), segments.to(
                            torch.device('mps')), \
                            masks.to(torch.device('mps')), labels.to(torch.device('mps'))
                    else:
                        inputs_id, segments, masks, labels = inputs_id.cuda(), segments.cuda(), masks.cuda(), labels.cuda()

                output, loss, _, _ = model(inputs_id, segments, masks, labels)
            else:

                inputs_id, labels, text_inputs = next(data_iter)

                curr_depth = np.array(labels[cur_depth]) if isinstance(labels[cur_depth], list) else labels[cur_depth]

                inputs_id, labels, = torch.LongTensor(inputs_id), torch.FloatTensor(curr_depth)

                if gpu[0] >= 0:
                    if torch.backends.mps.is_available():
                        inputs_id, labels, text_inputs = inputs_id.to(torch.device('mps')), labels.to(
                            torch.device('mps')), text_inputs.to(torch.device('mps'))
                    else:
                        inputs_id, labels, text_inputs = inputs_id.cuda(), labels.cuda(), text_inputs.cuda()

                output, loss, _, _ = model(inputs_id, labels, text_inputs)

            output = torch.sigmoid(output)
            output = output.data.cpu().numpy()

            losses.append(loss.item())
            target_data = labels.data.cpu().numpy()

            yhat_raw.append(output)
            # output = np.round(output)
            output = np.where(output > args.thres, 1, 0)
            y.append(target_data)
            yhat.append(output)

    y = np.concatenate(y, axis=0)
    yhat = np.concatenate(yhat, axis=0)
    yhat_raw = np.concatenate(yhat_raw, axis=0)

    k = [5, 8, 15]
    metrics = all_metrics(yhat, y, k=k, yhat_raw=yhat_raw)
    print_metrics(metrics)
    metrics['loss_%s' % fold] = np.mean(losses)
    return metrics
