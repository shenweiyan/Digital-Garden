---
title: 使用 Planemo 进行 Galaxy 工具开发
number: 57
slug: discussions-57/
url: https://github.com/shenweiyan/Digital-Garden/discussions/57
date: 2024-02-04
authors: [shenweiyan]
categories: 
  - 3.1-Galaxy
labels: ['3.1.x-GalaxyOther']
---

> 说明：本文章原文发布于 《[使用 Planemo 进行 Galaxy 工具开发 - 语雀](https://www.yuque.com/shenweiyan/biox/planemo-for-galaxy)》，部分内容已更新。

文章开始前，我们先了解一下 Planemo 到底是个什么东西。

> Command-line utilities to assist in developing [Galaxy](http://galaxyproject.org/) and [Common Workflow Language](https://www.commonwl.org/) artifacts - including tools, workflows, and training materials.

说白了，Planemo 就是用于 Galaxy 平台工具和 WDL 通用工作流语言相关产品辅助开发的一个命令行工具，这个程序集可以用于工具、流程，以及培训教材的开发。

<!-- more -->

## 安装 Planemo 

无论是 pip 还是 conda 都可以安装 Planemo：
```bash
$ pip install planemo
$ pip install -U git+git://github.com/galaxyproject/planemo.git
```
```bash
$ conda config --add channels bioconda
$ conda config --add channels conda-forge
$ conda install planemo
```

接下来，进入今天的正题，我们来详细介绍一下怎么使用 Planemo 进行 Galaxy 工具开发。

## 基础用法

本指南将演示如何使用 Heng Li 的 `Seqtk` 软件包构建命令工具，该软件包用于处理 FASTA 和 FASTQ 文件中的序列数据。

首先，我们需要先安装 `Seqtk` 。在这里，我们使用 `conda` 来安装 `Seqtk` (你也可以使用其他的方法安装)。
```bash
$ conda install --force --yes -c conda-forge -c bioconda seqtk=1.2
    ... seqtk installation ...
$ seqtk seq
        Usage:   seqtk seq [options] <in.fq>|<in.fa>
        Options: -q INT    mask bases with quality lower than INT [0]
                 -X INT    mask bases with quality higher than INT [255]
                 -n CHAR   masked bases converted to CHAR; 0 for lowercase [0]
                 -l INT    number of residues per line; 0 for 2^32-1 [0]
                 -Q INT    quality shift: ASCII-INT gives base quality [33]
                 -s INT    random seed (effective with -f) [11]
                 -f FLOAT  sample FLOAT fraction of sequences [1]
                 -M FILE   mask regions in BED or name list FILE [null]
                 -L INT    drop sequences with length shorter than INT [0]
                 -c        mask complement region (effective with -M)
                 -r        reverse complement
                 -A        force FASTA output (discard quality)
                 -C        drop comments at the header lines
                 -N        drop sequences containing ambiguous bases
                 -1        output the 2n-1 reads only
                 -2        output the 2n reads only
                 -V        shift quality by '(-Q) - 33'
```
接下来，我们将下载一个 FASTQ 示例文件，并测试一个简单的 Seqtk 命令 `seq` ，该命令将 FASTQ 文件转换为 FASTA。
```bash
$ wget https://raw.githubusercontent.com/galaxyproject/galaxy-test-data/master/2.fastq
$ seqtk seq -A 2.fastq > 2.fasta
$ cat 2.fasta
>EAS54_6_R1_2_1_413_324
CCCTTCTTGTCTTCAGCGTTTCTCC
>EAS54_6_R1_2_1_540_792
TTGGCAGGCCAAGGCCGATGGATCA
>EAS54_6_R1_2_1_443_348
GTTGCTTCTGGCGTGGGTGGGGGGG
```
有关功能齐全的 Seqtk 包封装，可以在 GitHub 上查看 [Helena Rasche's wrappers](https://github.com/galaxyproject/tools-iuc/tree/master/tools/seqtk)。

Galaxy 工具文件只是 XML 文件，因此此时可以打开文本编辑器并开始编写工具。Planemo 有一个命令 `tool_init` 可以快速生成一些样板 XML，因此首先开始。
```bash
$ planemo tool_init --id 'seqtk_seq' --name 'Convert to FASTA (seqtk)'
```
`tool_init` 命令可以采用各种复杂的参数，但如上面展示的 `--id` 和 `--name` 是其中两个最基本的参数。每个 Galaxy 工具都需要一个 ID（这是 Galaxy 自身用来标识该工具的简短标识符）和一个名称（此名称会显示给 Galaxy 用户，并且应该是该工具的简短描述）。工具名称可以包含空格，但其 ID 不能包含空格。

上面的命令将生成一个 seqtk_seq.xml 文件，这个文件看起来像这样：
```xml
<tool id="seqtk_seq" name="Convert to FASTA (seqtk)" version="0.1.0" python_template_version="3.5">
    <requirements>
    </requirements>
    <command detect_errors="exit_code"><![CDATA[
        TODO: Fill in command template.
    ]]></command>
    <inputs>
    </inputs>
    <outputs>
    </outputs>
    <help><![CDATA[
        TODO: Fill in help.
    ]]></help>
</tool>
```
这个生成的模板 XML 文件具有了 Galaxy 工具所需的公共部分内容，但你仍然需要打开编辑器并填写命令模板、输入参数描述、工具输出信息、帮助部分信息等。

`tool_init` 命令也可以做得更好。 们可以使用在 `seqtk seq -a 2.fastq> 2.fasta` 上面尝试过的测试命令作为示例，通过指定输入和输出来生成命令块，如下所示。
```bash
$ planemo tool_init --force \
                    --id 'seqtk_seq' \
                    --name 'Convert to FASTA (seqtk)' \
                    --requirement seqtk@1.2 \
                    --example_command 'seqtk seq -a 2.fastq > 2.fasta' \
                    --example_input 2.fastq \
                    --example_output 2.fasta
```
这将生成以下 XML 文件- 该文件具有正确的输入和输出定义以及实际的命令模板。
```xml
<tool id="seqtk_seq" name="Convert to FASTA (seqtk)" version="0.1.0" python_template_version="3.5">
    <requirements>
        <requirement type="package" version="1.2">seqtk</requirement>
    </requirements>
    <command detect_errors="exit_code"><![CDATA[
        seqtk seq -a '$input1' > '$output1'
    ]]></command>
    <inputs>
        <param type="data" name="input1" format="fastq" />
    </inputs>
    <outputs>
        <data name="output1" format="fasta" />
    </outputs>
    <help><![CDATA[
        TODO: Fill in help.
    ]]></help>
</tool>(
```
如本节开头所示，命令 `seqtk seq` 会为 `seq` 命令生成帮助消息。 `tool_init` 可以获取该帮助消息，并使用 `help_from_command` 选项将其正确粘贴在生成的工具 XML 文件中。

通常，命令帮助消息并不完全适用于工具，因为它们会提到参数名称和由工具抽象出来的类似细节，但它们可能是一个很好的起点。

以下 Planemo 的 `tool_init` 的调用已增强为使用 `--help_from_command`。
```bash
$ planemo tool_init --force \
                    --id 'seqtk_seq' \
                    --name 'Convert to FASTA (seqtk)' \
                    --requirement seqtk@1.2 \
                    --example_command 'seqtk seq -a 2.fastq > 2.fasta' \
                    --example_input 2.fastq \
                    --example_output 2.fasta \
                    --test_case \
                    --cite_url 'https://github.com/lh3/seqtk' \
                    --help_from_command 'seqtk seq'
```

除了演示 `--help_from_command` 之外，这还演示了使用 `--test_case` 从我们的示例生成测试用例并为基础工具添加引用。生成的工具 XML 文件为：
```xml
<tool id="seqtk_seq" name="Convert to FASTA (seqtk)" version="0.1.0" python_template_version="3.5">
    <requirements>
        <requirement type="package" version="1.2">seqtk</requirement>
    </requirements>
    <command detect_errors="exit_code"><![CDATA[
        seqtk seq -a '$input1' > '$output1'
    ]]></command>
    <inputs>
        <param type="data" name="input1" format="fastq" />
    </inputs>
    <outputs>
        <data name="output1" format="fasta" />
    </outputs>
    <tests>
        <test>
            <param name="input1" value="2.fastq"/>
            <output name="output1" file="2.fasta"/>
        </test>
    </tests>
    <help><![CDATA[

Usage:   seqtk seq [options] <in.fq>|<in.fa>

Options: -q INT    mask bases with quality lower than INT [0]
         -X INT    mask bases with quality higher than INT [255]
         -n CHAR   masked bases converted to CHAR; 0 for lowercase [0]
         -l INT    number of residues per line; 0 for 2^32-1 [0]
         -Q INT    quality shift: ASCII-INT gives base quality [33]
         -s INT    random seed (effective with -f) [11]
         -f FLOAT  sample FLOAT fraction of sequences [1]
         -M FILE   mask regions in BED or name list FILE [null]
         -L INT    drop sequences with length shorter than INT [0]
         -c        mask complement region (effective with -M)
         -r        reverse complement
         -A        force FASTA output (discard quality)
         -C        drop comments at the header lines
         -N        drop sequences containing ambiguous bases
         -1        output the 2n-1 reads only
         -2        output the 2n reads only
         -V        shift quality by '(-Q) - 33'
         -U        convert all bases to uppercases
         -S        strip of white spaces in sequences


    ]]></help>
    <citations>
        <citation type="bibtex">
@misc{githubseqtk,
  author = {LastTODO, FirstTODO},
  year = {TODO},
  title = {seqtk},
  publisher = {GitHub},
  journal = {GitHub repository},
  url = {https://github.com/lh3/seqtk},
}</citation>
    </citations>
</tool>
```

至此，我们有了一个功能相当齐全的 Galaxy 工具，它带有测试和帮助。这是一个非常简单的示例——通常，您需要在工具中投入更多工作才能实现这一点， `tool_init` 实际上只是为了让您入门而设计的。

现在让我们检查并测试我们开发的工具。Planemo的 `lint`（或仅 `l` ）命令将检查工具的 XML 有效性，检查是否有明显的错误以及是否符合 IUC 的最佳做法。
```bash
$ planemo l
Linting tool /opt/galaxy/tools/seqtk_seq.xml
Applying linter tests... CHECK
.. CHECK: 1 test(s) found.
Applying linter output... CHECK
.. INFO: 1 outputs found.
Applying linter inputs... CHECK
.. INFO: Found 1 input parameters.
Applying linter help... CHECK
.. CHECK: Tool contains help section.
.. CHECK: Help contains valid reStructuredText.
Applying linter general... CHECK
.. CHECK: Tool defines a version [0.1.0].
.. CHECK: Tool defines a name [Convert to FASTA (seqtk)].
.. CHECK: Tool defines an id [seqtk_seq].
.. CHECK: Tool targets 16.01 Galaxy profile.
Applying linter command... CHECK
.. INFO: Tool contains a command.
Applying linter citations... CHECK
.. CHECK: Found 1 likely valid citations.
Applying linter tool_xsd... CHECK
.. INFO: File validates against XML schema.
```
默认情况下， `lint` 会在您当前的工作目录中找到所有工具，但是我们可以使用 `planemo lint seqtk_seq.xml` 指定一个特定的工具。

接下来，我们可以使用 `test`（或仅执行 `t` ）命令运行工具的功能测试。这将打印很多输出（因为它启动了 Galaxy 实例），但最终应该显示我们通过的一项测试。

> 如果你的服务器已经安装了 Galaxy 实例，你可以编辑 ~/.planemo.yml 文件，指定 Galaxy 实例路径。

```yaml
## Specify a default galaxy_root for the `test` and `serve` commands here.
galaxy_root: /home/user/galaxy
```
> 完整的 `~/.planemo.yml` 示例，参考：[https://planemo.readthedocs.io/en/latest/configuration.html](https://planemo.readthedocs.io/en/latest/configuration.html)

```bash
$ planemo t
...
All 1 test(s) executed passed.
seqtk_seq[0]: passed
```
除了在控制台中将测试结果显示为红色（失败）或绿色（通过）外，Planemo 还默认为测试结果创建 HTML 报告。 还有更多测试报告选项可用，例如 `--test_output_xunit`，在某些持续集成环境中很有用。有关更多选项，请参见 `planemo test --help` ，以及 `test_reports` 命令。

现在，我们可以使用 `serve`（或仅使用 `s` ）命令打开 Galaxy。
```bash
$ planemo s
...
serving on http://127.0.0.1:9090
```

在网络浏览器中打开 [http://127.0.0.1:9090](http://127.0.0.1:9090) 以查看您的新工具。

服务和测试可以通过各种命令行参数传递，例如 `--galaxy_root`，以指定要使用的 Galaxy 实例（默认情况下，planemo 将仅为 planemo 下载和管理实例）。

## 简单参数

我们为 `seqtk seq` 命令构建了一个工具包的封装，但是该工具实际上具有我们可能希望向 Galaxy 用户公开的其他选项。

让我们从 `help` 命令中获取一些参数，并构建 Galaxy 的 `param` 块以粘贴到该工具的 `input` 块中。
```bash
-V        shift quality by '(-Q) - 33'
```

在上一节中，我们看到了输入文件在 `param` 块中是一个 `data` 的类型，除此之外我们还可以使用许多不同种类的参数。如标志参数（例如以上 `-V` 参数），通常在 Galaxy 工具的 XML 文件中由 `boolean` 来表示。
```xml
<param name="shift_quality" type="boolean" label="Shift quality"
       truevalue="-V" falsevalue=""
       help="shift quality by '(-Q) - 33' (-V)" />
```
然后，我们可以将 `$shift_quality` 粘贴在 `command` 块中，如果用户选择了此选项，它将扩展为 `-V` （因为我们已将其定义为 `truevalue` ）。如果用户未选择此选项，则 `$shift_quality` 将仅扩展为空字符串，而不会影响生成的命令行。

现在考虑以下的 `seqtk seq` 参数：
```bash
-q INT    mask bases with quality lower than INT [0]
-X INT    mask bases with quality higher than INT [255]
```

这些可以转换为 Galaxy 参数，如下所示：
```xml
<param name="quality_min" type="integer" label="Mask bases with quality lower than"
       value="0" min="0" max="255" help="(-q)" />
<param name="quality_max" type="integer" label="Mask bases with quality higher than"
       value="255" min="0" max="255" help="(-X)" />
```

这些可以作为 `-q $quality_min -X $quality_max` 添加到命令标签中。

此时，该工具将如下所示：
```xml
<tool id="seqtk_seq" name="Convert to FASTA (seqtk)" version="0.1.0" python_template_version="3.5">
    <requirements>
        <requirement type="package" version="1.2">seqtk</requirement>
    </requirements>
    <command detect_errors="exit_code"><![CDATA[
        seqtk seq
              $shift_quality
              -q $quality_min
              -X $quality_max
              -a '$input1' > '$output1'
    ]]></command>
    <inputs>
        <param type="data" name="input1" format="fastq" />
        <param name="shift_quality" type="boolean" label="Shift quality" 
               truevalue="-V" falsevalue=""
               help="shift quality by '(-Q) - 33' (-V)" />
        <param name="quality_min" type="integer" label="Mask bases with quality lower than" 
               value="0" min="0" max="255" help="(-q)" />
        <param name="quality_max" type="integer" label="Mask bases with quality higher than" 
               value="255" min="0" max="255" help="(-X)" />
    </inputs>
    <outputs>
        <data name="output1" format="fasta" />
    </outputs>
    <tests>
        <test>
            <param name="input1" value="2.fastq"/>
            <output name="output1" file="2.fasta"/>
        </test>
    </tests>
    <help><![CDATA[
        
Usage:   seqtk seq [options] <in.fq>|<in.fa>

Options: -q INT    mask bases with quality lower than INT [0]
         -X INT    mask bases with quality higher than INT [255]
         -n CHAR   masked bases converted to CHAR; 0 for lowercase [0]
         -l INT    number of residues per line; 0 for 2^32-1 [0]
         -Q INT    quality shift: ASCII-INT gives base quality [33]
         -s INT    random seed (effective with -f) [11]
         -f FLOAT  sample FLOAT fraction of sequences [1]
         -M FILE   mask regions in BED or name list FILE [null]
         -L INT    drop sequences with length shorter than INT [0]
         -c        mask complement region (effective with -M)
         -r        reverse complement
         -A        force FASTA output (discard quality)
         -C        drop comments at the header lines
         -N        drop sequences containing ambiguous bases
         -1        output the 2n-1 reads only
         -2        output the 2n reads only
         -V        shift quality by '(-Q) - 33'
         -U        convert all bases to uppercases


    ]]></help>
    <citations>
        <citation type="bibtex">
@misc{githubseqtk,
  author = {LastTODO, FirstTODO},
  year = {TODO},
  title = {seqtk},
  publisher = {GitHub},
  journal = {GitHub repository},
  url = {https://github.com/lh3/seqtk},
}</citation>
    </citations>
</tool>
```

## 条件参数

以前的参数很简单，因为它们总是出现，现在考虑一下下面的参数。
```bash
-M FILE   mask regions in BED or name list FILE [null]
```

我们可以通过添加属性 `optional ="true"` 将该数据类型参数标记为可选。
```xml
<param name="mask_regions" type="data" label="Mask regions in BED"
       format="bed" help="(-M)" optional="true" />
```

然后，不仅可以直接在命令块中使用 `$mask_regions`，还可以将其包装在 `if` 语句中（因为工具 XML 文件支持 [Cheetah](https://cheetahtemplate.org/users_guide/index.html)）。
```xml
#if $mask_regions
-M '$mask_regions'
#end if
```


接着，我们考虑这一组参数：
```bash
-s INT    random seed (effective with -f) [11]
-f FLOAT  sample FLOAT fraction of sequences [1]
```

在这种情况下，只有在设置了样本参数的情况下，才能看到或使用 `-s` 随机种子参数。我们可以使用 `conditional` 条件块来表达这一点。
```xml
<conditional name="sample">
    <param name="sample_selector" type="boolean" label="Sample fraction of sequences" />
    <when value="true">
        <param name="fraction" label="Fraction" type="float" value="1.0"
               help="(-f)" />
        <param name="seed" label="Random seed" type="integer" value="11"
               help="(-s)" />
    </when>
    <when value="false">
    </when>
</conditional>
```

在命令块中，我们可以再次使用 `if` 语句包括这些参数。
```xml
#if $sample.sample_selector
-f $sample.fraction -s $sample.seed
#end if
```

注意，我们必须使用 `sample.` 的前缀来引用这个参数，因为它们是在 `sample` 的条件块内定义的。

现在该工具的最新版本如下：
```xml
<tool id="seqtk_seq" name="Convert to FASTA (seqtk)" version="0.1.0" python_template_version="3.5">
    <requirements>
        <requirement type="package" version="1.2">seqtk</requirement>
    </requirements>
    <command detect_errors="exit_code"><![CDATA[
        seqtk seq
              $shift_quality
              -q $quality_min
              -X $quality_max
              #if $mask_regions
                  -M '$mask_regions'
              #end if
              #if $sample.sample
                  -f $sample.fraction
                  -s $sample.seed
              #end if
              -a '$input1' > '$output1'
    ]]></command>
    <inputs>
        <param type="data" name="input1" format="fastq" />
        <param name="shift_quality" type="boolean" label="Shift quality" 
               truevalue="-V" falsevalue=""
               help="shift quality by '(-Q) - 33' (-V)" />
        <param name="quality_min" type="integer" label="Mask bases with quality lower than" 
               value="0" min="0" max="255" help="(-q)" />
        <param name="quality_max" type="integer" label="Mask bases with quality higher than" 
               value="255" min="0" max="255" help="(-X)" />
        <param name="mask_regions" type="data" label="Mask regions in BED" 
               format="bed" help="(-M)" optional="true" />
        <conditional name="sample">
            <param name="sample" type="boolean" label="Sample fraction of sequences" />
            <when value="true">
                <param name="fraction" label="Fraction" type="float" value="1.0"
                       help="(-f)" />
                <param name="seed" label="Random seed" type="integer" value="11"
                       help="(-s)" />
            </when>
            <when value="false">
            </when>
        </conditional>
    </inputs>
    <outputs>
        <data name="output1" format="fasta" />
    </outputs>
    <tests>
        <test>
            <param name="input1" value="2.fastq"/>
            <output name="output1" file="2.fasta"/>
        </test>
    </tests>
    <help><![CDATA[
        
Usage:   seqtk seq [options] <in.fq>|<in.fa>

Options: -q INT    mask bases with quality lower than INT [0]
         -X INT    mask bases with quality higher than INT [255]
         -n CHAR   masked bases converted to CHAR; 0 for lowercase [0]
         -l INT    number of residues per line; 0 for 2^32-1 [0]
         -Q INT    quality shift: ASCII-INT gives base quality [33]
         -s INT    random seed (effective with -f) [11]
         -f FLOAT  sample FLOAT fraction of sequences [1]
         -M FILE   mask regions in BED or name list FILE [null]
         -L INT    drop sequences with length shorter than INT [0]
         -c        mask complement region (effective with -M)
         -r        reverse complement
         -A        force FASTA output (discard quality)
         -C        drop comments at the header lines
         -N        drop sequences containing ambiguous bases
         -1        output the 2n-1 reads only
         -2        output the 2n reads only
         -V        shift quality by '(-Q) - 33'
         -U        convert all bases to uppercases


    ]]></help>
    <citations>
        <citation type="bibtex">
@misc{githubseqtk,
  author = {LastTODO, FirstTODO},
  year = {TODO},
  title = {seqtk},
  publisher = {GitHub},
  journal = {GitHub repository},
  url = {https://github.com/lh3/seqtk},
}</citation>
    </citations>
</tool>
```
对于这样的工具，这些工具有很多选项，但在大多数情况下使用默认值是首选——一个常见的习惯用法是使用条件将参数分为简单部分和高级部分。

使用惯用法，更新此工具后的 XML 如下所示：
```xml
<tool id="seqtk_seq" name="Convert to FASTA (seqtk)" version="0.1.0" python_template_version="3.5">
    <requirements>
        <requirement type="package" version="1.2">seqtk</requirement>
    </requirements>
    <command detect_errors="exit_code"><![CDATA[
        seqtk seq
              #if $settings.advanced == "advanced"
                  $settings.shift_quality
                  -q $settings.quality_min
                  -X $settings.quality_max
                  #if $settings.mask_regions
                      -M '$settings.mask_regions'
                  #end if
                  #if $settings.sample.sample
                      -f $settings.sample.fraction
                      -s $settings.sample.seed
                  #end if
              #end if
              -a '$input1' > '$output1'
    ]]></command>
    <inputs>
        <param type="data" name="input1" format="fastq" />
        <conditional name="settings">
            <param name="advanced" type="select" label="Specify advanced parameters">
                <option value="simple" selected="true">No, use program defaults.</option>
                <option value="advanced">Yes, see full parameter list.</option>
            </param>
            <when value="simple">
            </when>
            <when value="advanced">
                <param name="shift_quality" type="boolean" label="Shift quality" 
                       truevalue="-V" falsevalue=""
                       help="shift quality by '(-Q) - 33' (-V)" />
                <param name="quality_min" type="integer" label="Mask bases with quality lower than" 
                       value="0" min="0" max="255" help="(-q)" />
                <param name="quality_max" type="integer" label="Mask bases with quality higher than" 
                       value="255" min="0" max="255" help="(-X)" />
                <param name="mask_regions" type="data" label="Mask regions in BED" 
                       format="bed" help="(-M)" optional="true" />
                <conditional name="sample">
                    <param name="sample" type="boolean" label="Sample fraction of sequences" />
                    <when value="true">
                        <param name="fraction" label="Fraction" type="float" value="1.0"
                               help="(-f)" />
                        <param name="seed" label="Random seed" type="integer" value="11"
                               help="(-s)" />
                    </when>
                    <when value="false">
                    </when>
                </conditional>
            </when>
        </conditional>
    </inputs>
    <outputs>
        <data name="output1" format="fasta" />
    </outputs>
    <tests>
        <test>
            <param name="input1" value="2.fastq"/>
            <output name="output1" file="2.fasta"/>
        </test>
    </tests>
    <help><![CDATA[
        
Usage:   seqtk seq [options] <in.fq>|<in.fa>

Options: -q INT    mask bases with quality lower than INT [0]
         -X INT    mask bases with quality higher than INT [255]
         -n CHAR   masked bases converted to CHAR; 0 for lowercase [0]
         -l INT    number of residues per line; 0 for 2^32-1 [0]
         -Q INT    quality shift: ASCII-INT gives base quality [33]
         -s INT    random seed (effective with -f) [11]
         -f FLOAT  sample FLOAT fraction of sequences [1]
         -M FILE   mask regions in BED or name list FILE [null]
         -L INT    drop sequences with length shorter than INT [0]
         -c        mask complement region (effective with -M)
         -r        reverse complement
         -A        force FASTA output (discard quality)
         -C        drop comments at the header lines
         -N        drop sequences containing ambiguous bases
         -1        output the 2n-1 reads only
         -2        output the 2n reads only
         -V        shift quality by '(-Q) - 33'
         -U        convert all bases to uppercases


    ]]></help>
    <citations>
        <citation type="bibtex">
@misc{githubseqtk,
  author = {LastTODO, FirstTODO},
  year = {TODO},
  title = {seqtk},
  publisher = {GitHub},
  journal = {GitHub repository},
  url = {https://github.com/lh3/seqtk},
}</citation>
    </citations>
</tool>
```

## 脚本封装

Tool Shed 上已经提供了许多常见的生物信息学应用程序，因此一项常见的开发任务是将各种复杂程度的脚本集成到 Galaxy 中。

考虑以下小型 Perl 脚本。
```perl
#!/usr/bin/perl -w

# usage : perl toolExample.pl <FASTA file> <output file>

open (IN, "<$ARGV[0]");
open (OUT, ">$ARGV[1]");
while (<IN>) {
    chop;
    if (m/^>/) {
        s/^>//;
        if ($. > 1) {
            print OUT sprintf("%.3f", $gc/$length) . "\n";
        }
        $gc = 0;
        $length = 0;
    } else {
        ++$gc while m/[gc]/ig;
        $length += length $_;
    }
}
print OUT sprintf("%.3f", $gc/$length) . "\n";
close( IN );
close( OUT );
```

可以按照以下步骤为此脚本构建 Galaxy 工具，并将脚本与工具 XML 文件本身放在同一目录中。这里的特殊值 `$__ tool_directory__` 是指工具（即 xml 文件）所在的目录。
```xml
<tool id="gc_content" name="Compute GC content">
  <description>for each sequence in a file</description>
  <command>perl '$__tool_directory__/gc_content.pl' '$input' output.tsv</command>
  <inputs>
    <param name="input" type="data" format="fasta" label="Source file"/>
  </inputs>
  <outputs>
    <data name="output" format="tabular" from_work_dir="output.tsv" />
  </outputs>
  <help>
This tool computes GC content from a FASTA file.
  </help>
</tool>
```

## Macros 宏集

如果您希望为单个相对简单的应用程序或脚本编写工具，则应跳过本节。如果您希望维护一系列相关工具——经验表明，您将意识到有很多重复的 XML 可以很好地做到这一点。Galaxy工具 XML 宏可以帮助减少这种重复。

通过使用 `--macros` 标志，Planemo 的 `tool_init` 命令可用于生成适合工具套件的宏文件。我们看一下以前的 `tool_init` 命令的变体（唯一的区别是现在我们添加了 `--macros` 标志）。
```bash
$ planemo tool_init --force \
                    --macros \
                    --id 'seqtk_seq' \
                    --name 'Convert to FASTA (seqtk)' \
                    --requirement seqtk@1.2 \
                    --example_command 'seqtk seq -A 2.fastq > 2.fasta' \
                    --example_input 2.fastq \
                    --example_output 2.fasta \
                    --test_case \
                    --help_from_command 'seqtk seq'
```
这将在当前目录中产生两个文件（ `seqtk_seq.xml` 和 `macros.xml`），而不是一个。
```xml
<tool id="seqtk_seq" name="Convert to FASTA (seqtk)" version="0.1.0" python_template_version="3.5">
    <macros>
        <import>macros.xml</import>
    </macros>
    <expand macro="requirements" />
    <command detect_errors="exit_code"><![CDATA[
        seqtk seq -A '$input1' > '$output1'
    ]]></command>
    <inputs>
        <param type="data" name="input1" format="fastq" />
    </inputs>
    <outputs>
        <data name="output1" format="fasta" />
    </outputs>
    <tests>
        <test>
            <param name="input1" value="2.fastq"/>
            <output name="output1" file="2.fasta"/>
        </test>
    </tests>
    <help><![CDATA[

Usage:   seqtk seq [options] <in.fq>|<in.fa>

Options: -q INT    mask bases with quality lower than INT [0]
         -X INT    mask bases with quality higher than INT [255]
         -n CHAR   masked bases converted to CHAR; 0 for lowercase [0]
         -l INT    number of residues per line; 0 for 2^32-1 [0]
         -Q INT    quality shift: ASCII-INT gives base quality [33]
         -s INT    random seed (effective with -f) [11]
         -f FLOAT  sample FLOAT fraction of sequences [1]
         -M FILE   mask regions in BED or name list FILE [null]
         -L INT    drop sequences with length shorter than INT [0]
         -c        mask complement region (effective with -M)
         -r        reverse complement
         -A        force FASTA output (discard quality)
         -C        drop comments at the header lines
         -N        drop sequences containing ambiguous bases
         -1        output the 2n-1 reads only
         -2        output the 2n reads only
         -V        shift quality by '(-Q) - 33'
         -U        convert all bases to uppercases
         -S        strip of white spaces in sequences


    ]]></help>
    <expand macro="citations" />
</tool>
```
```xml
<macros>
    <xml name="requirements">
        <requirements>
        <requirement type="package" version="1.2">seqtk</requirement>
            <yield/>
        </requirements>
    </xml>
    <xml name="citations">
        <citations>
            <yield />
        </citations>
    </xml>
</macros>
```

如您在上面的代码中所看到的，宏是可重用的 XML 块，它们使避免重复和保持 XML 简洁变得更加容易。


## 参考资料

- [Macros syntax](https://wiki.galaxyproject.org/Admin/Tools/ToolConfigSyntax#Reusing_Repeated_Configuration_Elements) on the Galaxy Wiki.
- [GATK tools](https://github.com/galaxyproject/tools-iuc/tree/master/tools/gatk2) (example tools making extensive use of macros)
- [gemini tools](https://github.com/galaxyproject/tools-iuc/tree/master/tools/gemini) (example tools making extensive use of macros)
- [bedtools tools](https://github.com/galaxyproject/tools-iuc/tree/master/tools/bedtools) (example tools making extensive use of macros)
- Macros implementation details - [Pull Request #129](https://bitbucket.org/galaxy/galaxy-central/pull-request/129/implement-macro-engine-to-reduce-tool/diff) and [Pull Request #140](https://bitbucket.org/galaxy/galaxy-central/pull-request/140/improvements-to-tool-xml-macroing-system/diff)
- [Galaxy’s Tool XML Syntax](https://docs.galaxyproject.org/en/latest/dev/schema.html)
- [Big List of Tool Development Resources](https://galaxyproject.org/develop/resources-tools/)
- [Cheetah templating](https://cheetahtemplate.org/users_guide/index.html)

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="57"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
