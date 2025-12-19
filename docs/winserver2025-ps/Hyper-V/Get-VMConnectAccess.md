---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmconnectaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMConnectAccess
---

# Get-VMConnectAccess

## 摘要
获取用户在多台Hyper-V主机上可连接的虚拟机列表。

## 语法

### VMName（默认值）
```
Get-VMConnectAccess [[-VMName] <String[]>] [-UserName <String[]>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMId
```
Get-VMConnectAccess [-VMId] <Guid[]> [-UserName <String[]>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

## 描述
`Get-VMConnectAccess` cmdlet 可用于获取显示用户及其能够连接的虚拟机信息的记录，这些虚拟机位于一个或多个 Hyper-V 主机上。该 cmdlet 的用途是为其他应用程序提供所需的权限，以便它们能够使用虚拟机连接协议（Virtual Machine Connection protocol）来发起会话。这类应用程序的示例包括 Virtual Machine Manager。

## 示例

### 示例 1
```
PS C:\> Get-VMConnectAccess
```

这个命令会获取所有具有权限连接到本地计算机上任何虚拟机的用户列表。示例假设之前已经为至少一个用户账户执行了“Grant-VMConnectAccess”操作。

### 示例 2
```
PS C:\> Get-VMConnectAccess -VMName VM1
```

这条命令会获取所有有权连接到虚拟机VM1的用户列表。示例假设之前已经为至少某个用户账户执行了“Grant-VMConnectAccess”命令，以授予其访问虚拟机VM1的权限。

### 示例 3
```
PS C:\> Get-VMConnectAccess -UserName CONTOSO\John
```

此命令会获取用户 Contoso\John 可以连接的所有本地计算机上的虚拟机的列表。示例假设之前已经运行了 `Grant-VMConnectAccess` 命令来授予 Contoso\John 连接这些虚拟机的权限。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全 Qualified Domain Name（FQDN）来进行识别。默认值为本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserName
指定正在查找连接访问权限的用户。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: UserId, Sid

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VMId
指定正在查找连接访问信息的虚拟机的唯一标识符。

```yaml
Type: Guid[]
Parameter Sets: VMId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -VMName
指定要查找连接访问信息的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMConnectAce

## 备注

## 相关链接

