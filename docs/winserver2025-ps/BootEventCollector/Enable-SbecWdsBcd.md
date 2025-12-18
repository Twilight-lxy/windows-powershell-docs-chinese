---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/enable-sbecwdsbcd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-SbecWdsBcd
---

# 启用-SbecWdsBcd

## 摘要
允许在导入到 WDS 服务器中的离线启动镜像中启用 BCD（二进制编码十进制）设置。

## 语法

### BcdPath
```
Enable-SbecWdsBcd -BcdPath <String[]> -CollectorIp <String> -CollectorPort <UInt32> -Key <String>
 [-BusParameters <String>] [-WdsRoot <String>] [-SkipNotifyWds] [<CommonParameters>]
```

### WdsImage
```
Enable-SbecWdsBcd [-Image <Array>] -CollectorIp <String> -CollectorPort <UInt32> -Key <String>
 [-BusParameters <String>] [-WdsRoot <String>] [-SkipNotifyWds] [<CommonParameters>]
```

## 描述
`Enable-SbecWdsBcd` 这个 cmdlet 可以启用导入到 WDS 服务器中的离线启动镜像中的引导配置数据（Boot Configuration Data，简称 BCD）设置。

在将一个启动镜像（例如通过**Enable-SbecBootImage**修改过的镜像）导入到Windows部署服务（WDS）后，WDS会自动生成相应的BCD配置文件。接下来，必须在该配置中启用对启动事件的支持功能。由于这个BCD文件具有特殊的格式，因此需要手动进行相关的设置才能使其正常工作。

由于 WDS 不支持为每个客户端单独生成 BCD 文件，因此如果多个客户端共享相同的 BCD 文件，它们就必须使用相同的密钥来与 Boot Event Collector 进行通信。解决这个问题的方法是使用一个通用的密钥来进行设置：这个通用密钥可以始终在收集器配置中指定为所有计算机的第二个通用密钥；或者也可以仅为即将进行设置的计算机添加到收集器配置中，在设置完成后将其删除。

在修改了 BCD 文件之后，必须通知 WDS 服务（或重新启动该服务），以便它能够获取到这些已修改的文件。除非另有指示，否则这个 cmdlet 会执行相应的通知操作。

## 示例

### 示例 1：在 WDS 中更新启动镜像
```
PS C:\> Get-WdsBootImage | Enable-SbecWdsBcd -CollectorIp "192.168.1.1" -CollectorPort 50000 -Key "a.b.c.d"
```

此命令适用于WDS中的所有启动镜像。

### 示例 2：更新一个 BCD 文件
```
PS C:\> Enable-SbecWdsBcd -BcdPath "c:\tmp\boot.wim.bcd" -CollectorIp "192.168.1.1" -CollectorPort 50000 -Key "a.b.c.d" -SkipNotifyWds
```

此命令用于更新从 WDS 复制的 BCD 文件中的设置。

## 参数

### -BcdPath
指定每个图像对应的BCD文件的明确路径。

```yaml
Type: String[]
Parameter Sets: BcdPath
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -BusParameters
指定用于选择目标计算机的网络接口卡（NIC）以进行通信的总线参数。此值会覆盖系统默认选择的第一个受支持的适配器。该设置适用于所有使用此镜像的计算机，但前提是这些计算机的硬件配置必须足够一致。要查找某台计算机上特定网络接口卡的总线参数，请打开“设备管理器”，在“网络适配器”中选择所需的网络适配器，右键单击该适配器，选择“属性”，然后进入“详细信息”选项卡，再选择“位置信息”。系统会显示一个格式为“PCI 总线 X，设备 Y，功能 Z”的字符串。本例中需要指定的总线参数即为 “X,Y,Z”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: BusParams

Required: False
Position: Named
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
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CollectorPort
指定端口号（该端口号通常同时用于目标系统和数据收集系统）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Image
指定通过 `Get-WdsBootImage` 命令获取的 Windows 部署服务 (WDS) 启动镜像对象。如果一个哈希表包含了 `Architecture` 和 `FileName` 属性，你也可以直接使用该哈希表来代替对象。

```yaml
Type: Array
Parameter Sets: WdsImage
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Key
指定用于通信的加密密钥。该值必须与针对此目标在收集器配置中指定的密钥相匹配。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipNotifyWds
表示此操作不会将文件更改的信息通知给WDS服务。

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

### -WdsRoot
指定 WDS 目录树的根目录。默认情况下，此值是从导出的 SMB 共享资源（REMINST）的路径中获取的。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_WdsBootImage
这个cmdlet的输入是从**Get-WdsBootImage**命令中获得的Windows部署服务（WDS）启动图像对象。如果你能提供一个包含“Architecture”和“FileName”属性的手动构建的哈希表，也可以直接使用该哈希表作为输入对象。

## 输出

### 没有（需要处理的内容）。

## 备注

## 相关链接

[Enable-SbecBcd](./Enable-SbecBcd.md)

[Enable-SbecBootImage](./Enable-SbecBootImage.md)

[New-SbecUnattendFragment](./New-SbecUnattendFragment.md)

