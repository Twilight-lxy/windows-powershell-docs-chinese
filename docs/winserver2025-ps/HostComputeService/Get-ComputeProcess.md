---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HostCompute.PowerShell.Cmdlets.dll-Help.xml
Module Name: HostComputeService
ms.date: 12/21/2016
online version: https://learn.microsoft.com/powershell/module/hostcomputeservice/get-computeprocess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-ComputeProcess
---

# Get-ComputeProcess

## 摘要
从 Hyper-V 主机计算服务中获取正在运行的计算系统的列表。

## 语法

### 过滤器（默认设置）
```
Get-ComputeProcess [[-Name] <String[]>] [-Owner <String[]>] [-Type <ComputeProcessType[]>] [<CommonParameters>]
```

### ID
```
Get-ComputeProcess [-Id] <String[]> [<CommonParameters>]
```

## 描述
`Get-ComputeProcess` cmdlet 从 Hyper-V 主机计算服务中获取正在运行的计算系统列表，其中包括虚拟机和容器。

你必须从提升权限的 PowerShell 会话中运行此cmdlet。

## 示例


## 参数

### -Id
指定一个计算系统ID数组，该cmdlet将从这个数组中获取所需的信息。

```yaml
Type: String[]
Parameter Sets: Id
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定此cmdlet获取的计算系统的名称。

```yaml
Type: String[]
Parameter Sets: Filters
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Owner
指定管理客户端，该客户端拥有此cmdlet所获取的计算系统。

```yaml
Type: String[]
Parameter Sets: Filters
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Type
指定此cmdlet获取的计算系统类型。该参数的可接受值为：VirtualMachine和Container。

```yaml
Type: ComputeProcessType[]
Parameter Sets: Filters
Aliases:
Accepted values: Container, VirtualMachine

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Stop-ComputeProcess](./Stop-ComputeProcess.md)

