import styled from 'styled-components'
import { livros } from '../UltimosLancamentos/dadosUltimosLancamentos'
import { Titulo } from '../Titulo'
import CardRecomenda from '../CardRecomenda'
import imagenLivro from '../../imagens/livro2.png'

const UltimosLancamentosContainer = styled.section`
    background-color: #EBECEE;
    padding-bottom: 20px;
    display: flex;
    flex-direction: column;
`
const NovosLivrosContainer = styled.div`
    margin-top: 30px;
    display: flex;
    width: 100%;
    justify-content: center;
    cursor: pointer;
`


function UltimosLancamentos() {
    return (
        <UltimosLancamentosContainer>
            <Titulo cor="#EB9B00">Ultimos Lançamentos</Titulo>
            <NovosLivrosContainer>
                {livros.map ( livro => (
                    <img src={livro.src}
                    />
                ))}
            </NovosLivrosContainer>
            <CardRecomenda
                titulo="Talvez você se interesse por"
                subTitulo="Angula 11"
                descricao="Construindo uma aplicação com a plataforma Google."
                img={imagenLivro}
            />
        </UltimosLancamentosContainer>
    )
}

export default UltimosLancamentos
