---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VM
---

# Get-VM

## 摘要
从一台或多台Hyper-V主机中获取虚拟机信息。

## 语法

### 名称（默认值）
```
Get-VM [[-Name] <String[]>] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [<CommonParameters>]
```

### ID
```
Get-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [[-Id] <Guid>]
 [<CommonParameters>]
```

### ClusterObject
```
Get-VM [-ClusterObject] <PSObject> [<CommonParameters>]
```

## 描述
`Get-VM` cmdlet 用于从一个或多个 Hyper-V 主机上获取虚拟机。

## 示例

### 示例 1
```
PS C:\> Get-VM
```

这个示例会获取本地虚拟机主机上的所有虚拟机。

### 示例 2
```
PS C:\> Get-VM -ComputerName Server1 | Where-Object {$_.State -eq 'Running'}
```

这个示例会获取Hyper-V主机Server1上所有正在运行的虚拟机。

### 示例 3
```
PS C:\> Get-ClusterGroup | ? {$_.GroupType -eq 'VirtualMachine' } | Get-VM
```

这个示例会获取集群中所有与本地Hyper-V主机相连的虚拟机。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClusterObject
指定要检索的虚拟机所属的集群资源或集群组。

```yaml
Type: PSObject
Parameter Sets: ClusterObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于获取虚拟机的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: True
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定要检索的虚拟机的标识符。

```yaml
Type: Guid
Parameter Sets: Id
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Name
指定要检索的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: Name
Aliases: VMName

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: True
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShellVirtualMachine

## 备注

## 相关链接

