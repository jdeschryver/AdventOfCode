import java.io.File

/**
 * @author Jan De Schryver <Jan.DeSchryver@bucephalus.be>
 */

// 2 december 2015

fun calculatePaper(box: String): Int {
    val params = box.split('x').map { it.toInt() }
    val s1 = params[0] * params[1]
    val s2 = params[1] * params[2]
    val s3 = params[2] * params[0]

    return 2 * (s1 + s2 + s3) + minOf(s1, s2, s3)
}

fun calculateRibbon(box: String): Int {
    val params = box.split('x').map { it.toInt() }
    val bow = listOf(params[0], params[1], params[2]).sorted()
    return (params[0] * params[1] * params[2]) + bow[0] * 2 + bow[1] * 2
}

fun main(args: Array<String>) {
    val input = File( "src\\main\\kotlin\\input.txt")
            .inputStream()
            .use { it.bufferedReader().readLines() }

    println(input.sumBy { calculatePaper(it) })
    println(input.sumBy { calculateRibbon(it) })

}

