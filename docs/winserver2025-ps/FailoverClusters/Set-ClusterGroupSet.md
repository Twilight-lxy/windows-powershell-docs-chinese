---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterCollection.cdxml-help.xml
Module Name: FailoverClusters
ms.date: 10/21/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/set-clustergroupset?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-ClusterGroupSet
---

# Set-ClusterGroupSet

## 摘要
更新集群组集合。

## 语法

### 查询（cdxml）（默认值）

```
Set-ClusterGroupSet [[-Name] <String[]>] [-StartupSetting <StartupSettingType>]
 [-StartupCount <UInt32>] [-IsGlobal <Boolean>] [-StartupDelay <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject (cdxml)

```
Set-ClusterGroupSet -InputObject <CimInstance[]> [-StartupSetting <StartupSettingType>]
 [-StartupCount <UInt32>] [-IsGlobal <Boolean>] [-StartupDelay <UInt32>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述

`Set-ClusterGroupSet` cmdlet 用于更新集群组集合。要更新集合中的群组，请使用 `Add-ClusterGroupToSet` 和 `Remove-ClusterGroupFromSet` cmdlet；要更新依赖关系，请使用 `Add-ClusterGroupSetDependency` 和 `Remove-ClusterGroupSetDependency` cmdlet。

## 示例

### 示例 1：将某个组设置更改为指定的启动设置

```powershell
Set-ClusterGroupSet -Name "Set002" -StartupDelayTrigger Online
```

这个命令将名为“Set002”的组设置为启动模式“Online”。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用 `*-Job` 系列的 cmdlets；要获取作业结果，则可以使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession

在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定在管道命令中使用的输入对象。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -IsGlobal

表示此 cmdlet 将该组设置为全局性的（即在整个系统中都适用）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

指定组集的名称。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -StartupCount

指定需要满足“准备就绪”状态的组数。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Count

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartupDelay

指定在达到“就绪”状态后需要等待的时间（以秒为单位）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases: Delay

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartupSetting

该参数用于指定设备组准备好启动时的具体启动设置。如果设置了延迟，那么只有在**StartupCount**参数中指定的所有组都完成启动过程（且未超过**StartupDelay**参数所设定的延迟时间）后，设备才会真正启动；如果设备需要处于在线状态才能启动，那么只有当**StartupCount**参数中的所有组都成功上线后，设备才会启动。

该参数的可接受值为：`Delay` 或 `Online`。

```yaml
Type: StartupSettingType
Parameter Sets: (All)
Aliases: StartupDelayTrigger
Accepted values: Delay, Online

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值`0`，Windows PowerShell会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最佳限制值。此限制仅适用于当前运行的cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-ClusterGroupSet](./Get-ClusterGroupSet.md)

[New-ClusterGroupSet](./New-ClusterGroupSet.md)

[Remove-ClusterGroupSet](./Remove-ClusterGroupSet.md)
