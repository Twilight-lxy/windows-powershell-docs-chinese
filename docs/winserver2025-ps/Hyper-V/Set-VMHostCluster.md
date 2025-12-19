---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmhostcluster?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMHostCluster
---

# Set-VMHostCluster

## 摘要
配置虚拟机主机集群。

## 语法

### `ClusterName`（默认值）
```
Set-VMHostCluster [-ClusterName] <String[]> [[-Credential] <PSCredential[]>] [-SharedStoragePath <String>]
 [-Passthru] [<CommonParameters>]
```

### CimSession
```
Set-VMHostCluster [-CimSession] <CimSession[]> [-SharedStoragePath <String>] [-Passthru] [<CommonParameters>]
```

### InputObject
```
Set-VMHostCluster [-InputObject] <VMHostCluster[]> [-SharedStoragePath <String>] [-Passthru]
 [<CommonParameters>]
```

## 描述
`Set-VMHostCluster` cmdlet 用于配置虚拟机主机集群。

## 示例

### 示例 1：配置虚拟机主机集群
```
PS C:\> Set-VMHostCluster -ClusterName "ContosoCluster" -SharedStoragePath "D:\ClusterStorage\cluster01"
```

此命令为名为 ContosoCluster 的集群配置了共享存储路径。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ClusterName
指定一个虚拟机主机集群名称数组，该cmdlet将针对这些集群进行配置。

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

### -InputObject
指定一个虚拟机主机集群数组，该cmdlet将配置这些集群。要获取一个**VMHostCluster**对象，请使用**Get-VMHostCluster** cmdlet。

```yaml
Type: VMHostCluster[]
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Passthru
表示此 cmdlet 返回它所配置的 **Microsoft.HyperV.PowerShell.VMHostCluster** 对象。

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

### -SharedStoragePath
指定虚拟机主机集群所使用的共享存储的位置。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMHostCluster
如果指定了 `Passthru` 参数，此 cmdlet 会返回一个 `VMHostCluster` 对象。

## 备注

## 相关链接

[Get-VMHostCluster](./Get-VMHostCluster.md)

