{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a5d085ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "\n",
    "import tensorflow as tf\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "def prediction(params):\n",
    "    model = tf.keras.models.load_model('models/mn_model_nn')\n",
    "    pred = model.predict([params])\n",
    "    return pred\n",
    "\n",
    "@app.route('/', methods=['POST', 'GET'])\n",
    "def predict():\n",
    "    message = ''\n",
    "    if request.method == 'POST':\n",
    "        param_list = ('Плотность, кг/м3', 'модуль упругости, ГПа', 'Количество отвердителя, м.%', \n",
    "                      'Содержание эпоксидных групп,%_2', 'Температура вспышки, С_2', 'Поверхностная плотность, г/м2\t', \n",
    "                      'Модуль упругости при растяжении, ГПа', 'Прочность при растяжении, МПа', 'Потребление смолы, г/м2',\n",
    "                      'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки')\n",
    "        params = []\n",
    "        for i in param_list:\n",
    "            param = request.form.get(i)\n",
    "            params.append(param)\n",
    "        params = [float(i.replace(',', '.')) for i in params]\n",
    "\n",
    "        message = f'Соотношение матрица-наполнитель: {prediction(params)}'\n",
    "    return render_template('mn.html', message=message)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "560995f4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
