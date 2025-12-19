---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmhostcluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMHostCluster
---

# Get-VMHostCluster

## 摘要
获取虚拟机主机集群信息。

## 语法

### `ClusterName`（默认值）
```
Get-VMHostCluster [-ClusterName] <String[]> [[-Credential] <PSCredential[]>] [<CommonParameters>]
```

### CimSession
```
Get-VMHostCluster [-CimSession] <CimSession[]> [<CommonParameters>]
```

## 描述
`Get-VMHostCluster` cmdlet 用于获取 `VMHostCluster` 对象。

## 示例

#### 示例 1：获取虚拟机主机集群
```
PS C:\> Get-VMHostCluster -ClusterName "ContosoCluster"
```

此命令用于获取名为 ContosoCluster 的集群对应的 **VMHostCluster** 对象。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ClusterName
指定一个包含虚拟机主机集群名称的数组，该数组是此 cmdlet 所获取的数据来源。

```yaml
Type: String[]
Parameter Sets: ClusterName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: ClusterName
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMHostCluster
此cmdlet返回一个**VMHostCluster**对象。

## 备注

## 相关链接

[Set-VMHostCluster](./Set-VMHostCluster.md)

