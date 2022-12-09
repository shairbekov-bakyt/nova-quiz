import axios from "axios";
import { warn } from "console";
import React, { useEffect } from "react";
import "./index.scss";
import { IQuiz } from "./interface";


function Result({ score, repeateGame, length }: { score: number; repeateGame: any; length:number;}) {
  return (
    <div className="result">
      <img src="https://cdn-icons-png.flaticon.com/512/2278/2278992.png" />
      <h2>
        Вы отгадали {score} ответа из {length}
      </h2>
      <button onClick={repeateGame}>Попробовать снова</button>
    </div>
  );
}

function Game({
  step,
  question,
  onClickVariant,
  length
}: {
  step: number;
  question: IQuiz;
  onClickVariant: any;
  length: number;
}) {
  const percentage = Math.round((step / length) * 100);
  return (
    <>
      <div className="progress">
        <div
          style={{ width: `${percentage}%` }}
          className="progress__inner"
        ></div>
      </div>
      <h1>{question.title}</h1>
      <ul>
         {question.variant.map((obj, index) => (
          <li onClick={() => onClickVariant(obj.id)} key={index}>
            {obj.question}
          </li>
        ))}
      </ul>
    </>
  );
}

function App() {
  const [questions, setQuestion] = React.useState<IQuiz[]>([])
  const [score, setScore] = React.useState(0)
  const [step, setStep] = React.useState(0);

  useEffect(() => {
    axios.get("http://0.0.0.0:8000/api/v1/quiz/")
    .then(response => {
        setQuestion(response.data)
      })
    .catch(err => console.log(err))
  }, [])

  const onClickVariant = (index: number) => {
    if (index === questions[step].correct) {
      setScore(score + 1);
    }
    setStep(step + 1);

  };

  const repeateGame = () => {
    setScore(0);
    setStep(0);
  };
  const question = questions[step]
  return (
    <div className="App">
      { step !== questions.length ? (
        <Game step={step} question={question} onClickVariant={onClickVariant} length={questions.length}/> 
      ) : (
        <Result score={score} repeateGame={repeateGame} length={questions.length} />
      )}
    </div>
  );
}

export default App;
