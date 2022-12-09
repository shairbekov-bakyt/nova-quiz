
export interface IQuiz {
  title: string
  variant: IVariant[]
  correct: number
}

export interface IVariant {
  id: number
  question: string
}


