#!/usr/bin/node

/*lets code*/
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
