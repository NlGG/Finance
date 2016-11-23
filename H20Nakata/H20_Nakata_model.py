# -*- coding: utf-8 -*-

import numpy as np
from sklearn.svm import SVC


def make_input(data):
    ndata = len(data)

    if ndata <= 5:
        return "Error"

    case_A = np.array([np.zeros(len(data[0])) for i in range(ndata - 1)])

    for i in range(ndata - 1):
        case_A[i] = data[i + 1] - data[i]

    case_B = np.array([np.zeros(len(data[0])) for i in range(ndata - 5)])

    for i in range(ndata - 5):
        case_B[i] = data[i + 5] - \
            sum([(11 - 2 * j) * data[i + 5 - j] / 25 for j in range(1, 6)])

    case_C = np.array([np.zeros(len(data[0])) for i in range(ndata - 5)])

    for i in range(ndata - 5):
        case_C[i] = data[i + 5] - \
            sum([(6 - j) * data[i + 5 - j] / 15 for j in range(1, 6)])

    case_D = np.array([np.zeros(len(data[0])) for i in range(ndata - 5)])

    for i in range(ndata - 5):
        case_D[i] = data[i + 5] - \
            sum([data[i + 5 - j] / 5 for j in range(1, 6)])

    return case_A, case_B, case_C, case_D


def make_label(data):
    ndata = len(data)

    label = np.zeros(ndata - 1)

    for i in range(ndata - 1):
        result = data[i + 1] - data[i]
        if result > 0:
            label[i] = 1
        else:
            label[i] = 0

    return label


class PredictDirection_PriceChanges:

    def __init__(self, x, y, pred, library=1):
        self.library = library
        self.x = x
        self.num_x = len(x)
        self.y = y
        self.pred = pred.reshape(1, -1)

        if self.library == 1:
            self.SVM = self.SVM_scikit
        else:
            self.SVM = self.SVM_original

    def tuning(self):
        s, c, val = self.grid_search()

        print(s, c, val)

        s, c, val = self.nelder_mead(s, c, val)

        return s, c, val

    def grid_search(self):
        lnsigma = np.array(range(-10, 11))
        lnC = np.array(range(-10, 11))

        val = 0

        for lns in lnsigma:
            for lnc in lnC:
                s = np.exp(lns)
                c = np.exp(lnc)

                srate = self.validation(s, c)

                print("(lnsigma^2, lnC)=",  (lns, lnc),  "識別誤り率=",  1 - srate)

                if val < srate:
                    val = srate
                    s_best = s
                    c_best = c

        self.grid_sigma = s_best
        self.grid_c = c_best

        return s_best, c_best, val

    def nelder_mead(self, s, c, val):
        alpha = 1
        gamma = 2
        beta = 1 / 2

        k = 10

        s_minus = (1 / 2) * (np.exp(np.log(s)) - np.exp(np.log(s) - 1))
        s_plus = (1 / 2) * (np.exp(np.log(s) + 1) - np.exp(np.log(s)))

        c_minus = (1 / 2) * (np.exp(np.log(c)) - np.exp(np.log(c) - 1))
        c_plus = (1 / 2) * (np.exp(np.log(c) + 1) - np.exp(np.log(c)))

        x_list = np.array([[np.random.uniform(s - s_minus, s + s_plus),
                            np.random.uniform(c - c_minus, c + c_plus)] for i in range(k)])
        val_list = np.array(
            [self.validation(x_list[i][0], x_list[i][1]) for i in range(k)])

        rank_val = np.argsort(val_list)

        x_list = np.array([x_list[r] for r in rank_val])

        val_list = np.sort(val_list)

        x_g = sum(x_list[1:]) / (k - 1)
        val_g = self.validation(x_g[0], x_g[1])

        x_l = x_list[0]
        val_l = val_list[0]
        x_h = x_list[1]
        val_h = val_list[1]

        x_k = (1 + alpha) * x_g - alpha * x_l
        val_k = self.validation(x_k[0], x_k[1])

        std_val = 100

        i = 0

        while std_val > 0.005:

            if val_k >= val_h:
                if val_k < val_list[-1]:
                    x_list[0] = x_k
                    val_list[0] = val_k
                    rank_val = np.argsort(val_list)
                    x_list = np.array([x_list[r] for r in rank_val])
                    val_list = np.sort(val_list)
                else:
                    x_e = (1 + gamma) * x_g - gamma * x_l
                    val_e = self.validation(x_e[0], x_e[1])

                    if val_e > val_k:
                        x_list[0] = x_e
                        val_list[0] = val_e
                        rank_val = np.argsort(val_list)
                        x_list = np.array([x_list[r] for r in rank_val])
                        val_list = np.sort(val_list)
                    else:
                        x_list[0] = x_k
                        val_list[0] = val_k
                        rank_val = np.argsort(val_list)
                        x_list = np.array([x_list[r] for r in rank_val])
                        val_list = np.sort(val_list)
            else:
                if val_k <= val_l:
                    x_c = beta * x_l + (1 - beta) * x_g
                else:
                    x_c = beta * x_k + (1 - beta) * x_g

                val_c = self.validation(x_c[0], x_c[1])

                if val_c > val_l:
                    x_list[0] = x_g
                    val_list[0] = val_g
                    rank_val = np.argsort(val_list)
                    x_list = np.array([x_list[r] for r in rank_val])
                    val_list = np.sort(val_list)
                else:
                    x_list = x_list + 1 / 2

            std_val = np.std(val_list)

            i += 1

            if i == 30:
                break

        print("Nelder Meadのiterationは", i, "回")

        s = x_list[-1][0]
        c = x_list[-1][1]

        return s, c, val

    def main(self, tun=1, sigma=0.01, C=0.5):
        x = self.x
        y = self.y
        pred = self.pred

        if tun == 1:
            s, c, val = self.tuning()
        else:
            s = sigma
            c = C
            val = self.validation(s, c)

        self.SVM(x, y, s, c)
        pred = self.estimator.predict(pred)
        print(pred)

        self.result = [s, c, val]

        return s, c, val

    def validation(self, sigma, C):
        if sigma < 0:
            sigma = 0.001

        x = self.x
        y = self.y

        success = 0.0
        window_num = round(self.num_x / 10)

        for i in range(10):
            pred_x = x[window_num * i:window_num * (i + 1)]
            obs_x = np.append(x[:window_num * i], x[window_num * (i + 1):], 0)

            label_pred_y = y[window_num * i:window_num * (i + 1)]
            label_y = np.append(y[:window_num * i], y[window_num * (i + 1):])

            self.SVM(obs_x, label_y, sigma, C)

            for j in range(len(pred_x)):
                # caution!
                if label_pred_y[j] == self.estimator.predict(pred_x[j].reshape(1, -1)):
                    success += 1.0

        return success / (window_num * 10)

    def SVM_scikit(self, x, y, sigma, C):
        self.estimator = SVC(C=C, gamma=1 / (2 * sigma), kernel='rbf',)
        self.estimator.fit(x, y)

    def descript(self, test_x, test_y, grid=True):
        s = self.result[0]
        c = self.result[1]

        x = self.x
        y = self.y

        self.SVM(x, y, s, c)

        success = 0.0

        predict_result = np.array([np.zeros(2) for i in range(2)])

        for i in range(len(test_x)):
            # caution!
            if test_y[i] == self.estimator.predict(test_x[i].reshape(1, -1)):
                success += 1.0
                if test_y[i] == 1:
                    predict_result[0][0] += 1
                else:
                    predict_result[1][1] += 1
            else:
                if test_y[i] == 1:
                    predict_result[1][0] += 1
                else:
                    predict_result[0][1] += 1

        success_rate = success / len(test_x)

        print("lnσ^2=", np.log(s))
        print("lnC=", np.log(c))
        print("識別誤り率は", 1 - self.result[2])
        print("識別成功率は", success_rate)

        print(predict_result)

        if grid is True:
            self.SVM(x, y, self.grid_sigma, self.grid_c)

        grid_success = 0.0

        predict_result = np.array([np.zeros(2) for i in range(2)])

        for i in range(len(test_x)):
            if test_y[i] == self.estimator.predict(test_x[i].reshape(1, -1)):
                grid_success += 1.0
                if test_y[i] == 1:
                    predict_result[0][0] += 1
                else:
                    predict_result[1][1] += 1
            else:
                if test_y[i] == 1:
                    predict_result[1][0] += 1
                else:
                    predict_result[0][1] += 1

        grid_success_rate = grid_success / len(test_x)

        print("グリッドサーチ最高点での識別成功率は", grid_success_rate)

        return success_rate
