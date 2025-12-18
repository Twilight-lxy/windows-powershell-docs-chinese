---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/new-sbecunattendfragment?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-SbecUnattendFragment
---

# New-SbecUnattendFragment

## 摘要
创建一个用于 Unattend.xml 的片段，其中包含安装后的命令。

## 语法

```
New-SbecUnattendFragment [-CollectorIp] <String> [-CollectorPort] <UInt32> [-Key] <String>
 [[-BusParameters] <String>] [[-Logger] <String[]>] [[-PermLogger] <String[]>] [-NoDefaultLoggers]
 [[-LogDbgMask] <UInt32>] [[-FirstOrder] <UInt32>] [<CommonParameters>]
```

## 描述
`New-SbecUnattendFragment` cmdlet 用于为 `Unattend.xml` 文件创建一个包含安装后命令的片段。你可以使用这些命令来配置你正在准备的镜像中的安装过程（Setup）和启动事件（Boot Event）监控功能。

生成的片段表示 `<RunSynchronous>` 元素的文本内容。该元素通常被插入到 Unattend.xml 文件中的 `<Component name="Microsoft-Windows-Setup">` 部分，位于 `<DiskConfiguration>` 之后。

生成的代码片段依赖于通过 `Enable-SbecBootImage` 命令在 WinPE 启动映像中创建的 `winpeshl.ini` 文件，没有这个文件的话，代码片段将无法正常运行。

此cmdlet返回的哈希表包含以下元素：

- `<UnattendText>`.
Text of the XML fragment for insertion into Unattend.xml, as an array of strings.
- `<NextOrder>`.
The next uint32 value for `<Order>` in case if you want to add more commands to the fragment.
See the description of the *FirstOrder* parameter for more information.

## 示例


## 参数

### -BusParameters
指定用于选择目标计算机的网络适配器（NIC）以进行通信的总线参数。此值会覆盖系统默认选择的第一个可用适配器。该设置适用于所有使用该镜像的计算机，但只有当这些计算机的硬件配置足够一致时才能生效。

要找到机器上某个特定网卡（NIC）的总线参数值，请打开“设备管理器”，在“网络适配器”中选择所需的设备。右键单击该设备，选择“属性”，然后选择“详细信息”选项卡，再选择“位置信息”。系统会显示如下格式的字符串：PCI总线X，设备Y，功能Z。在这个例子中需要指定的总线参数就是“X,Y,Z”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: BusParams

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CollectorIp
指定托管“启动事件收集器”（Boot Event Collector）的主机的IPv4地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CollectorPort
指定端口号（该端口号码通常同时用于目标服务器和数据收集器）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FirstOrder
指定用于开始自动生成命令编号的值。

`Unattend.xml` 文件中的命令必须按照 `<Order>` 元素中指定的顺序进行排列。默认情况下，命令的顺序是从 1 开始的；但如果你添加了自己的自定义命令，那么系统自动生成的命令就必须使用一个更大的序列号作为起始值。

如果您指定了这个参数，即使其值为 1，生成的 XML 片段的文本也不会包含外部的 `<RunSynchronous>` 元素。因为您可能希望从多个部分组装该元素。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Key
指定用于通信的加密密钥。该值必须与为此目标配置的收集器中指定的密钥相匹配。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogDbgMask
指定用于“调试打印过滤器”位掩码（Debug Print Filter bit mask）的值，该掩码可用于启用来自 **DbgPrint**() 函数的消息。必须设置 0x1 位，以便能够显示包含错误检查（Bugcheck）系统崩溃信息的消息。如果将掩码设置为 0，则不会生成用于设置此注册表值的命令。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Logger
指定要启用转发的 AutoLogger 会话。这些会话上的转发功能在操作系统启动后会自动失效。如果在 *Logger* 或 *PermLogger* 中明确指定了某个会话，将会覆盖该会话的默认设置。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoDefaultLoggers
表示此操作不会自动添加默认的日志记录器会话集。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PermLogger
指定要启用转发的 AutoLogger 会话。这些会话的转发功能在操作系统启动后仍然保持启用状态。如果在 *Logger* 或 *PermLogger* 中明确指定了某个会话，那么该会话的相关默认设置将被覆盖。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 哈希表
此cmdlet返回一个哈希表，其中包含以下元素：

- `<UnattendText>`.
Text of the XML fragment to insert into Unattend.xml as an array of strings.
- `<NextOrder>`.
The next uint32 value for `<Order>` if you want to add more commands to the fragment.
For more information, see the *FirstOrder* parameter.

## 备注

## 相关链接

[Enable-SbecAutologger](./Enable-SbecAutologger.md)

[Enable-SbecBootImage](./Enable-SbecBootImage.md)

[Enable-SbecWdsBcd](./Enable-SbecWdsBcd.md)

