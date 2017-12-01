/**
 * @author Jan De Schryver <Jan.DeSchryver@bucephalus.be>
 */
// 1 december 2017

fun decodeCaptcha(captcha: String, l: Int = captcha.length / 2) =
        captcha.filterIndexed({i, c -> captcha[(i + l) % captcha.length] == c})
                .sumBy { it.toRealInt() }

fun Char.toRealInt() = this - '0'

fun main(args:Array<String>) {
    val captcha = "111233"
    println(decodeCaptcha(captcha, 1))
    println(decodeCaptcha(captcha))
}