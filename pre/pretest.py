import util.ioutil as ioutil

f_train_x_lines, f_train_y_lines, f_test_x_lines = ioutil.read_train_test()

print len(f_train_x_lines), len(f_train_y_lines), len(f_test_x_lines)
